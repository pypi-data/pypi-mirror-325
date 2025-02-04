import json
import logging
from pathlib import Path

from pyFAI import method_registry
from pyFAI.io import ponifile
from ewokscore import Task

from .utils import pyfai_utils, xrpd_utils

__all__ = ["PyFaiConfig"]

logger = logging.getLogger(__name__)


class PyFaiConfig(
    Task,
    optional_input_names=[
        "filename",
        "filenames",
        "energy",
        "geometry",
        "mask",
        "flatfield",
        "darkcurrent",
        "darkflatmethod",
        "detector",
        "detector_config",
        "calibrant",
        "integration_options",
    ],
    output_names=[
        "energy",
        "geometry",
        "detector",
        "detector_config",
        "calibrant",
        "mask",
        "flatfield",
        "darkcurrent",
        "integration_options",
    ],
):
    """Parse pyFAI calibration and integration parameters"""

    def run(self):
        input_values = self.get_input_values()
        integration_options = self.merged_integration_options()

        if "poni" in integration_options and integration_options.get("version", 0) > 3:
            integration_options.update(integration_options.pop("poni"))

        wavelength = integration_options.pop("wavelength", None)
        energy = input_values.get("energy", None) or integration_options.pop(
            "energy", None
        )
        if energy is None:
            if wavelength is not None:
                energy = xrpd_utils.energy_wavelength(wavelength)

        detector = integration_options.pop("detector", None)
        if not self.missing_inputs.detector:
            detector = input_values["detector"]

        detector_config = integration_options.pop("detector_config", None)
        if not self.missing_inputs.detector_config:
            detector_config = input_values["detector_config"]

        calibrant = input_values.get("calibrant", None)

        mask = input_values.get("mask", None)
        flatfield = input_values.get("flatfield", None)
        darkcurrent = input_values.get("darkcurrent", None)
        if not self.missing_inputs.darkflatmethod:
            integration_options["darkflatmethod"] = self.inputs.darkflatmethod

        geometry = {
            k: integration_options.pop(k)
            for k in ["dist", "poni1", "poni2", "rot1", "rot2", "rot3"]
            if k in integration_options
        }
        if not self.missing_inputs.geometry:
            geometry = input_values["geometry"]

        do_poisson = integration_options.pop("do_poisson", None)
        do_azimuthal_error = integration_options.pop("do_azimuthal_error", None)
        error_model = integration_options.pop("error_model", None)
        if not error_model:
            if do_poisson:
                error_model = "poisson"
            if do_azimuthal_error:
                error_model = "azimuthal"
        if error_model:
            integration_options["error_model"] = error_model

        # Check method and integrator function
        method = integration_options.get("method", "")
        if not isinstance(method, str):
            method = "_".join(method)
        pmethod = method_registry.Method.parsed(method)

        integrator_name = integration_options.get("integrator_name", "")
        if integrator_name in ("sigma_clip", "_sigma_clip_legacy"):
            logger.warning(
                "'%s' is not compatible with the pyfai worker: use 'sigma_clip_ng'",
                integrator_name,
            )
            integration_options["integrator_name"] = "sigma_clip_ng"
        if "sigma_clip_ng" == integrator_name and pmethod.split != "no":
            raise ValueError(
                "to combine sigma clipping with pixel splitting, use 'sigma_clip_legacy'"
            )

        # Split integration and worker options
        self.outputs.energy = energy
        self.outputs.geometry = geometry
        self.outputs.detector = detector
        self.outputs.detector_config = detector_config
        self.outputs.calibrant = calibrant
        self.outputs.mask = mask
        self.outputs.flatfield = flatfield
        self.outputs.darkcurrent = darkcurrent
        self.outputs.integration_options = integration_options

    def merged_integration_options(self) -> dict:
        """Merge integration options in this order of priority:

        - filename (lowest priority)
        - filenames[0]
        - filenames[1]
        - ...
        - integration_options (highest priority)
        """
        integration_options = dict()
        filenames = list()
        if self.inputs.filename:
            filenames.append(self.inputs.filename)
        if self.inputs.filenames:
            filenames.extend(self.inputs.filenames)
        for filename in filenames:
            integration_options.update(pyfai_utils.read_config(filename))
        if self.inputs.integration_options:
            integration_options.update(
                pyfai_utils.normalize_parameters(self.inputs.integration_options)
            )
        return integration_options


class SavePyFaiConfig(
    Task,
    input_names=[
        "output_filename",
        "energy",
        "geometry",
        "detector",
    ],
    optional_input_names=[
        "mask",
        "detector_config",
        "integration_options",
    ],
    output_names=["filename"],
):
    """Save inputs as pyFAI calibration and integration configuration file (.json)

    The configuration is saved as a JSON file following pyFAI configuration format.

    Required inputs:
    - output_filename (str): Name of the file where to save pyFAI configuration. Must include the extension
    - energy (float): Energy in KeV
    - geometry (dict): pyFAI geometry information (poni)
    - detector (str): Name of the detector

    Optional inputs:
    - mask (str): Filename of the mask to used
    - detector_config (dict): Configuration of the detector
    - integration_options (dict): Extra configuration fields

    Outputs:
    - filename (str): Saved filename, same as output_filename
    """

    def run(self):
        integration_options = pyfai_utils.normalize_parameters(
            self.get_input_value("integration_options", {})
        )
        version = integration_options.pop("version", 3)

        config = {
            "application": "pyfai-integrate",
            "version": version,
        }

        wavelength = xrpd_utils.energy_wavelength(self.inputs.energy)

        if version > 4:  # pyFAI >= v2025.0
            raise NotImplementedError(f"pyFAI config version {version} not supported")

        if version == 4:  # pyFAI = v2024.09
            poni = _create_ponifile(
                wavelength,
                self.inputs.geometry,
                self.inputs.detector,
                self.get_input_value("detector_config", {}),
            )
            config["poni"] = poni.as_dict()
        else:
            # Add entries as pyFAI
            config["wavelength"] = wavelength
            config.update(self.inputs.geometry)
            config["detector"] = self.inputs.detector
            config["detector_config"] = self.get_input_value("detector_config", None)

        mask = self.get_input_value("mask", None)
        if mask is not None:
            config["do_mask"] = True
            config["mask_file"] = mask

        for key, value in integration_options.items():
            config.setdefault(key, value)  # Do not override already set keys

        filepath = Path(self.inputs.output_filename).absolute()
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(json.dumps(config, indent=4))

        self.outputs.filename = str(filepath)


class SavePyFaiPoniFile(
    Task,
    input_names=[
        "output_filename",
        "energy",
        "geometry",
        "detector",
    ],
    optional_input_names=[
        "detector_config",
    ],
    output_names=["filename"],
):
    """Save inputs as pyFAI PONI file

    Required inputs:
    - output_filename (str): Name of the file where to save pyFAI PONI. Must include extension.
    - energy (float): Energy in KeV
    - geometry (dict): pyFAI geometry information (poni)
    - detector (str): Name of the detector

    Optional inputs:
    - detector_config (dict): Configuration of the detector

    Outputs:
    - filename (str): Saved filename, same as output_filename
    """

    def run(self):
        poni = _create_ponifile(
            xrpd_utils.energy_wavelength(self.inputs.energy),
            self.inputs.geometry,
            self.inputs.detector,
            self.get_input_value("detector_config", {}),
        )

        filepath = Path(self.inputs.output_filename).absolute()
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with filepath.open("w", encoding="ascii") as fd:
            poni.write(fd)

        self.outputs.filename = str(filepath)


def _create_ponifile(
    wavelength: float,
    geometry: dict,
    detector: str,
    detector_config: dict,
) -> ponifile.PoniFile:
    return ponifile.PoniFile(
        {
            **geometry,  # First so other fields overrides it
            "detector": detector,
            "detector_config": detector_config,
            "wavelength": wavelength,
        }
    )

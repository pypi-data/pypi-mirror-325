import json
from pyFAI.io.ponifile import PoniFile

from ..tasks.pyfaiconfig import SavePyFaiConfig, SavePyFaiPoniFile

from orangecontrib.ewoksxrpd.savepyfaiconfig import OWSavePyFaiConfig
from orangecontrib.ewoksxrpd.savepyfaiponifile import OWSavePyFaiPoniFile

from ewoks import execute_graph
from ewoksorange.tests.utils import execute_task


def test_pyfai_config_roundtrip(tmp_path, setup1):
    """Create and save pyFAI configuration"""
    workflow = {
        "graph": {"id": "test_roundtrip"},
        "nodes": [
            {
                "id": "load",
                "task_type": "class",
                "task_identifier": "ewoksxrpd.tasks.pyfaiconfig.PyFaiConfig",
            },
            {
                "id": "save",
                "task_type": "class",
                "task_identifier": "ewoksxrpd.tasks.pyfaiconfig.SavePyFaiConfig",
            },
        ],
        "links": [
            {
                "source": "load",
                "target": "save",
                "data_mapping": [
                    {"source_output": "energy", "target_input": "energy"},
                    {"source_output": "geometry", "target_input": "geometry"},
                    {"source_output": "detector", "target_input": "detector"},
                    {
                        "source_output": "detector_config",
                        "target_input": "detector_config",
                    },
                    {"source_output": "mask", "target_input": "mask"},
                    {
                        "source_output": "integration_options",
                        "target_input": "integration_options",
                    },
                ],
            },
        ],
    }

    output_path = tmp_path / "pyfaiconfig.json"
    mask_filename = str(tmp_path / "mask.edf")
    integration_options = {
        "error_model": "poisson",
    }
    result = execute_graph(
        workflow,
        inputs=[
            {"id": "load", "name": "energy", "value": setup1.energy},
            {"id": "load", "name": "geometry", "value": setup1.geometry},
            {"id": "load", "name": "mask", "value": mask_filename},
            {"id": "load", "name": "detector", "value": setup1.detector},
            {"id": "load", "name": "detector_config", "value": setup1.detector_config},
            {"id": "load", "name": "integration_options", "value": integration_options},
            {"id": "save", "name": "output_filename", "value": str(output_path)},
        ],
        outputs=[{"all": False}],
    )
    assert result["filename"] == str(output_path)
    expected_config = {
        "application": "pyfai-integrate",
        "version": 3,
        "wavelength": setup1.wavelength,
        "detector": setup1.detector,
        "do_mask": True,
        "mask_file": mask_filename,
        "detector_config": setup1.detector_config,
        **setup1.geometry,
        **integration_options,
    }
    config = json.loads(output_path.read_text())
    assert config == expected_config


def test_SavePyFaiConfig(tmp_path, setup1, qtapp):
    output_path = tmp_path / "pyfaiconfig.json"
    integration_options = {
        "error_model": "poisson",
    }
    mask_filename = str(tmp_path / "mask.edf")
    inputs = {
        "output_filename": str(output_path),
        "energy": setup1.energy,
        "geometry": setup1.geometry,
        "detector": setup1.detector,
        "mask": mask_filename,
        "detector_config": setup1.detector_config,
        "integration_options": integration_options,
    }

    result = execute_task(
        SavePyFaiConfig if qtapp is None else OWSavePyFaiConfig,
        inputs=inputs,
    )

    assert result["filename"] == str(output_path)
    expected_config = {
        "application": "pyfai-integrate",
        "version": 3,
        "wavelength": setup1.wavelength,
        "detector": setup1.detector,
        "do_mask": True,
        "mask_file": mask_filename,
        "detector_config": setup1.detector_config,
        **setup1.geometry,
        **integration_options,
    }
    config = json.loads(output_path.read_text())
    assert config == expected_config


def test_SavePyFaiConfig_v4(tmp_path, setup1, qtapp):
    output_path = tmp_path / "pyfaiconfig.json"

    bad_poni_info = {
        **setup1.geometry,
        "wavelength": 0.0,
        "detector": "BAD_DETECTOR",
        "detector_config": {"orientation": 1},
    }
    integration_options = {
        "application": "pyfai-integrate",
        "version": 4,
        "error_model": "poisson",
        "poni": bad_poni_info,
    }

    mask_filename = str(tmp_path / "mask.edf")
    inputs = {
        "output_filename": str(output_path),
        "energy": setup1.energy,
        "geometry": setup1.geometry,
        "detector": setup1.detector,
        "mask": mask_filename,
        "detector_config": setup1.detector_config,
        "integration_options": integration_options,
    }

    result = execute_task(
        SavePyFaiConfig if qtapp is None else OWSavePyFaiConfig,
        inputs=inputs,
    )

    assert result["filename"] == str(output_path)
    expected_config = {
        "application": "pyfai-integrate",
        "version": 4,
        "poni": {
            **setup1.geometry,
            "poni_version": 2.1,
            "wavelength": setup1.wavelength,
            "detector": setup1.detector,
            "detector_config": setup1.detector_config,
        },
        "do_mask": True,
        "mask_file": mask_filename,
        "error_model": "poisson",
    }
    config = json.loads(output_path.read_text())
    assert config == expected_config


def test_SavePyFaiPoniFile(tmp_path, setup1, qtapp):
    output_path = tmp_path / "pyfaiconfig.json"

    inputs = {
        "output_filename": str(output_path),
        "energy": setup1.energy,
        "geometry": setup1.geometry,
        "detector": setup1.detector,
        "detector_config": setup1.detector_config,
    }

    result = execute_task(
        SavePyFaiPoniFile if qtapp is None else OWSavePyFaiPoniFile,
        inputs=inputs,
    )

    assert result["filename"] == str(output_path)

    result_poni = PoniFile(result["filename"])
    expected_poni = PoniFile(
        {
            "wavelength": setup1.wavelength,
            **setup1.geometry,
            "detector": setup1.detector,
            "detector_config": setup1.detector_config,
        }
    )
    assert result_poni.as_dict() == expected_poni.as_dict()

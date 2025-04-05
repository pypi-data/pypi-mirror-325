from copy import deepcopy
import pathlib
import pytest

from pyaerocom.aeroval.modelmaps_engine import ModelMapsEngine
from pyaerocom.aeroval import EvalSetup
from pyaerocom.exceptions import ModelVarNotAvailable
from pyaerocom import GriddedData
from tests.fixtures.aeroval.cfg_test_exp1 import CFG


@pytest.fixture(scope="function")
def cfg(tmpdir: pathlib.Path):
    cfg = deepcopy(CFG)
    cfg["json_basedir"] = f"{tmpdir}/data"
    cfg["coldata_basedir"] = f"{tmpdir}/coldata"

    return cfg


def test__process_map_var(cfg: dict):
    stp = EvalSetup(**cfg)
    engine = ModelMapsEngine(stp)
    with pytest.raises(ModelVarNotAvailable) as excinfo:
        engine._process_contour_map_var("LOTOS", "concco", False)

    assert "Cannot read data for model LOTOS" in str(excinfo.value)


def test__run(caplog, cfg: dict):
    stp = EvalSetup(**cfg)
    engine = ModelMapsEngine(stp)
    engine.run(model_list=["TM5-AP3-CTRL"], var_list=["conco"])
    assert "no data for model TM5-AP3-CTRL, skipping" in caplog.text


def test__run_working(caplog, cfg: dict):
    stp = EvalSetup(**cfg)
    engine = ModelMapsEngine(stp)
    files = engine.run(model_list=["TM5-AP3-CTRL"], var_list=["od550aer"])
    assert any([f.endswith("data/test/exp1/contour/od550aer_TM5-AP3-CTRL.geojson") for f in files])


@pytest.mark.parametrize(
    "maps_freq, result",
    [("monthly", "monthly"), ("yearly", "yearly"), ("coarsest", "yearly")],
)
def test__get_maps_freq(maps_freq, result, cfg: dict):
    cfg["maps_freq"] = maps_freq
    stp = EvalSetup(**cfg)
    engine = ModelMapsEngine(stp)
    freq = engine._get_maps_freq()

    assert freq == result


@pytest.mark.parametrize(
    "maps_freq,result,ts_types",
    [
        ("monthly", "monthly", ["daily", "monthly", "yearly"]),
        ("yearly", "yearly", ["daily", "monthly", "yearly"]),
        ("coarsest", "yearly", ["daily", "monthly", "yearly"]),
        ("coarsest", "monthly", ["hourly", "daily", "monthly"]),
        ("coarsest", "daily", ["weekly", "daily"]),
    ],
)
def test__get_read_model_freq(maps_freq, result, ts_types, cfg: dict):
    cfg["maps_freq"] = maps_freq
    stp = EvalSetup(**cfg)
    engine = ModelMapsEngine(stp)
    freq = engine._get_read_model_freq(ts_types)

    assert freq == result


@pytest.mark.parametrize(
    "maps_freq,ts_types,errormsg",
    [
        (
            "daily",
            ["monthly", "yearly"],
            "Could not find any model data for given maps_freq.*",
        ),
    ],
)
def test__get_read_model_freq_error(maps_freq, ts_types, errormsg, cfg: dict):
    cfg["maps_freq"] = maps_freq
    stp = EvalSetup(**cfg)
    engine = ModelMapsEngine(stp)

    with pytest.raises(ValueError, match=errormsg):
        engine._get_read_model_freq(ts_types)


def test__read_model_data(cfg: dict):
    model_name = "TM5-AP3-CTRL"
    var_name = "od550aer"
    stp = EvalSetup(**cfg)
    engine = ModelMapsEngine(stp)

    data = engine._read_model_data(model_name, var_name)

    assert isinstance(data, GriddedData)

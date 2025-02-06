import sys
import xml.etree.ElementTree as ET
from collections.abc import Iterable
from math import pi, sin, sqrt
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pytest
from component_model.model import Model
from fmpy import plot_result, simulate_fmu
from fmpy.util import fmu_info
from fmpy.validation import validate_fmu
from libcosimpy.CosimEnums import CosimExecutionState
from libcosimpy.CosimExecution import CosimExecution
from libcosimpy.CosimLogging import CosimLogLevel, log_output_level
from libcosimpy.CosimManipulator import CosimManipulator
from libcosimpy.CosimObserver import CosimObserver
from libcosimpy.CosimSlave import CosimLocalSlave

from sim_explorer.utils.misc import from_xml
from sim_explorer.utils.osp import make_osp_system_structure
from tests.data.Oscillator.driving_force_fmu import DrivingForce, func
from tests.data.Oscillator.oscillator_fmu import HarmonicOscillator


def check_expected(
    value: Any,  # noqa: ANN401
    expected: Any,  # noqa: ANN401
    feature: str,
):
    if isinstance(expected, float):
        assert abs(value - expected) < 1e-10, f"Expected the {feature} '{expected}', but found the value {value}"
    else:
        assert value == expected, f"Expected the {feature} '{expected}', but found the value {value}"


def arrays_equal(
    res: Iterable[Any],
    expected: Iterable[Any],
    eps: float = 1e-7,
):
    len_res = len(list(res))
    len_exp = len(list(expected))
    if len_res != len_exp:
        raise ValueError(f"Arrays of different lengths cannot be equal. Found {len_res} != {len_exp}")
    for i, (x, y) in enumerate(zip(res, expected, strict=False)):
        assert abs(x - y) < eps, f"Element {i} not nearly equal in {x}, {y}"


def do_show(time: list[float], z: list[float], v: list[float]):
    fig, ax = plt.subplots()
    _ = ax.plot(time, z, label="z-position")
    _ = ax.plot(time, v, label="z-speed")
    _ = ax.legend()
    plt.show()


def force(t: float, ampl: float = 1.0, omega: float = 0.1):
    return np.array((0, 0, ampl * sin(omega * t)), dtype=float)


@pytest.fixture(scope="session")
def oscillator_fmu():
    return _oscillator_fmu()


def _oscillator_fmu():
    """Make FMU and return .fmu file with path."""
    build_path = Path(__file__).parent / "data" / "Oscillator"
    build_path.mkdir(exist_ok=True)
    src = Path(__file__).parent / "data" / "Oscillator" / "oscillator_fmu.py"
    fmu_path = Model.build(
        script=str(src),
        project_files=[src],
        dest=build_path,
    )
    return fmu_path


@pytest.fixture(scope="session")
def driver_fmu():
    return _oscillator_fmu()


def _driver_fmu():
    """Make FMU and return .fmu file with path."""
    build_path = Path(__file__).parent / "data" / "Oscillator"
    build_path.mkdir(exist_ok=True)
    src = Path(__file__).parent / "data" / "Oscillator" / "driving_force_fmu.py"
    fmu_path = Model.build(
        script=str(src),
        project_files=[src],
        dest=build_path,
    )
    print("DRIVER", fmu_path)
    return fmu_path


@pytest.fixture(scope="session")
def system_structure():
    return _system_structure()


def _system_structure():
    """Make a OSP structure file and return the path"""
    path = make_osp_system_structure(
        name="ForcedOscillator",
        simulators={
            "osc": {"source": "HarmonicOscillator.fmu", "stepSize": 0.01},
            "drv": {"source": "DrivingForce.fmu", "stepSize": 0.01},
        },
        connections_variable=[("drv", "f[2]", "osc", "f[2]")],
        version="0.1",
        start=0.0,
        base_step=0.01,
        algorithm="fixedStep",
        path=Path(__file__).parent / "data" / "Oscillator",
    )

    return path


def test_oscillator_force_class(show: bool):
    """Test the HarmonicOscillator and DrivingForce classes in isolation.

    The first four lines are necessary to ensure that the Oscillator class can be accessed:
    If pytest is run from the command line, the current directory is the package root,
    but when it is run from the editor (__main__) it is run from /tests/.
    """

    osc = HarmonicOscillator(k=1.0, c=0.1, m=1.0)

    osc.x[2] = 1.0
    times = []
    z = []
    v = []
    #    _f = partial(force, ampl=1.0, omega=0.1)
    dt = 0.01
    time = 0.0
    assert abs(2 * pi / sqrt(osc.k / osc.m) - 2 * pi) < 1e-9, f"Period should be {2 * pi}"
    for _ in range(10000):
        osc.f = func(time=time)
        _ = osc.do_step(time=time, dt=dt)
        times.append(time)
        z.append(osc.x[2])
        v.append(osc.v[2])
        time += dt

    if show:
        do_show(time=times, z=z, v=v)

    dri = DrivingForce()
    assert osc.c == 0.1
    assert dri.ampl == 1.0
    arrays_equal(res=func(time=1.0), expected=(0, 0, sin(0.1)))


def test_make_fmus(
    oscillator_fmu: Path,
    driver_fmu: Path,
):
    info = fmu_info(filename=str(oscillator_fmu))  # this is a formatted string. Not easy to check
    print(f"Info Oscillator: {info}")
    val = validate_fmu(filename=str(oscillator_fmu))
    assert not len(val), f"Validation of of {oscillator_fmu.name} was not successful. Errors: {val}"

    info = fmu_info(filename=str(driver_fmu))  # this is a formatted string. Not easy to check
    print(f"Info Driver: {info}")
    val = validate_fmu(filename=str(driver_fmu))
    assert not len(val), f"Validation of of {oscillator_fmu.name} was not successful. Errors: {val}"


def test_make_system_structure(system_structure: Path):
    assert Path(system_structure).exists(), "System structure not created"
    el = from_xml(Path(system_structure))
    assert isinstance(el, ET.Element), f"ElementTree element expected. Found {el}"
    ns = el.tag.split("{")[1].split("}")[0]
    print("NS", ns)
    for s in el.findall(".//{*}Simulator"):
        assert (Path(system_structure).parent / s.get("source", "??")).exists(), f"Component {s.get('name')} not found"
    for _con in el.findall(".//{*}VariableConnection"):
        for c in _con:
            assert c.attrib in ({"simulator": "drv", "name": "f[2]"}, {"simulator": "osc", "name": "f[2]"})


def test_use_fmu(oscillator_fmu: Path, driver_fmu: Path, show: bool):
    """Test single FMUs."""
    # sourcery skip: move-assign
    result = simulate_fmu(
        oscillator_fmu,
        stop_time=50,
        step_size=0.01,
        validate=True,
        solver="Euler",
        debug_logging=True,
        logger=print,  # fmi_call_logger=print,
        start_values={"x[2]": 1.0, "c": 0.1},
        step_finished=None,  # pyright: ignore[reportArgumentType]  # (typing incorrect in fmpy)
        fmu_instance=None,  # pyright: ignore[reportArgumentType]  # (typing incorrect in fmpy)
    )
    if show:
        plot_result(result)


def test_run_osp(oscillator_fmu: Path, driver_fmu: Path):
    # sourcery skip: extract-duplicate-method
    sim = CosimExecution.from_step_size(step_size=1e8)  # empty execution object with fixed time step in nanos
    osc = CosimLocalSlave(fmu_path=str(oscillator_fmu), instance_name="osc")
    _osc = sim.add_local_slave(osc)
    assert _osc == 0, f"local slave number {_osc}"
    reference_dict = {var_ref.name.decode(): var_ref.reference for var_ref in sim.slave_variables(_osc)}

    dri = CosimLocalSlave(fmu_path=str(driver_fmu), instance_name="dri")
    _dri = sim.add_local_slave(dri)
    assert _dri == 1, f"local slave number {_dri}"

    # Set initial values
    sim.real_initial_value(slave_index=_osc, variable_reference=reference_dict["x[2]"], value=1.0)
    sim.real_initial_value(slave_index=_osc, variable_reference=reference_dict["c"], value=0.1)

    sim_status = sim.status()
    assert sim_status.current_time == 0
    assert CosimExecutionState(sim_status.state) == CosimExecutionState.STOPPED

    # Simulate for 1 second
    _ = sim.simulate_until(target_time=15e9)


@pytest.mark.skipif(sys.platform.startswith("linux"), reason="HarmonicOsciallator.fmu throws an error on Linux")
def test_run_osp_system_structure(system_structure: Path, show: bool):
    "Run an OSP simulation in the same way as the SimulatorInterface of case_study is implemented"
    log_output_level(CosimLogLevel.TRACE)
    simulator = CosimExecution.from_osp_config_file(str(system_structure))
    sim_status = simulator.status()
    assert sim_status.current_time == 0
    assert CosimExecutionState(sim_status.state) == CosimExecutionState.STOPPED
    comps = []
    for comp in list(simulator.slave_infos()):
        name = comp.name.decode()
        comps.append(name)
    assert comps == ["osc", "drv"]
    variables = {}
    for idx in range(simulator.num_slave_variables(0)):
        struct = simulator.slave_variables(0)[idx]
        variables[struct.name.decode()] = {
            "reference": struct.reference,
            "type": struct.type,
            "causality": struct.causality,
            "variability": struct.variability,
        }

    for idx in range(simulator.num_slave_variables(1)):
        struct = simulator.slave_variables(1)[idx]
        variables |= {
            struct.name.decode(): {
                "reference": struct.reference,
                "type": struct.type,
                "causality": struct.causality,
                "variability": struct.variability,
            }
        }
    assert variables["c"]["type"] == 0
    assert variables["c"]["causality"] == 1
    assert variables["c"]["variability"] == 1

    assert variables["x[2]"]["type"] == 0
    assert variables["x[2]"]["causality"] == 2
    assert variables["x[2]"]["variability"] == 4

    assert variables["v[2]"]["type"] == 0
    assert variables["v[2]"]["causality"] == 2
    assert variables["v[2]"]["variability"] == 4

    # Instantiate a suitable observer for collecting results.
    # Instantiate a suitable manipulator for changing variables.
    manipulator = CosimManipulator.create_override()
    simulator.add_manipulator(manipulator=manipulator)
    simulator.real_initial_value(slave_index=0, variable_reference=1, value=0.5)
    simulator.real_initial_value(slave_index=0, variable_reference=5, value=1.0)
    observer = CosimObserver.create_last_value()
    simulator.add_observer(observer=observer)
    times = []
    pos = []
    speed = []
    for step in range(1, 1000):
        time = step * 0.01
        _ = simulator.simulate_until(step * 1e8)
        values = observer.last_real_values(slave_index=0, variable_references=[5, 8])
        # print(f"Time {simulator.status().current_time*1e-9}: {values}")
        times.append(time)
        pos.append(values[0])
        speed.append(values[1])
    if show:
        do_show(time=times, z=pos, v=speed)


# def test_sim_explorer(show):
#     cases = Cases( Path(__file__).parent / "data" / "Oscillator" / "ForcedOscillator.cases")
#     print("INFO", cases.info())
#     cases.run_case("base")
#     for c in ("base", "no_damping_no_force", "resonant"):
#         res = Results(file= Path(__file__).parent / "data" / "Oscillator" / (c+'.js5'))
#         if show:
#             res.plot_time_series('osc.x_z', f"Case {c}. z-position")

if __name__ == "__main__":
    retcode = pytest.main(args=["-rA", "-v", __file__, "--show", "True"])
    assert retcode == 0, f"Non-zero return code {retcode}"
    # import os
    # os.chdir(Path(__file__).parent.absolute() / "test_working_directory")
    # test_oscillator_force_class(show=True)
    # test_make_fmus(_oscillator_fmu(), _driver_fmu())
    # test_make_system_structure( _system_structure())
    # test_use_fmu(_oscillator_fmu(), _driver_fmu(), show=True)
    # test_run_osp(_oscillator_fmu(), _driver_fmu())
    # test_run_osp_system_structure(_system_structure(), show=True)
    # test_sim_explorer(show=True)

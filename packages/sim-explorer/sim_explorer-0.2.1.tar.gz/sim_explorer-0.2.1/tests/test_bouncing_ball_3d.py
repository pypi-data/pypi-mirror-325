from collections.abc import Sequence
from math import sqrt
from pathlib import Path
from typing import Any

import pytest
from fmpy import plot_result, simulate_fmu

from sim_explorer.case import Case, Cases


def arrays_equal(res: Sequence[Any], expected: Sequence[Any], eps: float = 1e-7):
    assert len(res) == len(expected), (
        f"Tuples of different lengths cannot be equal. Found {len(res)} != {len(expected)}"
    )
    for i, (x, y) in enumerate(zip(res, expected, strict=False)):
        assert abs(x - y) < eps, f"Element {i} not nearly equal in {x}, {y}"


def test_run_fmpy(show: bool):
    """Test and validate the basic BouncingBall using fmpy and not using OSP or sim_explorer."""
    path = Path(__file__).parent / "data" / "BouncingBall3D" / "BouncingBall3D.fmu"
    assert path.exists(), f"File {path} does not exist"
    dt = 0.01
    result = simulate_fmu(
        path,
        start_time=0.0,
        stop_time=3.0,
        step_size=dt,
        validate=True,
        solver="Euler",
        debug_logging=False,
        visible=True,
        logger=print,  # fmi_call_logger=print,
        start_values={
            "pos[2]": 10.0 * 0.0254,
            "speed[0]": 1.0,
            "e": 0.9,
            "g": 9.81,
        },
        step_finished=None,  # pyright: ignore[reportArgumentType]  # (typing incorrect in fmpy)
        fmu_instance=None,  # pyright: ignore[reportArgumentType]  # (typing incorrect in fmpy)
    )
    assert len(result)
    if show:
        plot_result(result)
    # no more testing than that. This is done in component-model tests


def check_case(  # noqa: C901, PLR0913, PLR0915
    cases: Cases,
    casename: str,
    stepSize: float = 0.01,
    stopTime: float = 3,
    g: float = 9.81,
    e: float = 1.0,
    x_z: float = 1 / 0.0254,  # this is in inch => 1m!
    hf: float = 0.0254,  # transformation m->inch
):
    """Run case 'name' and check results with respect to key issues."""
    case = cases.case_by_name(name=casename)
    assert isinstance(case, Case), f"Case {case} does not seem to be a proper case object"
    dt = case.special["stepSize"]
    tfac = int(1 / dt)
    print(f"Run case {case.name}. g={g}, e={e}, x_z={x_z}, dt={dt}")
    case.run()  # run the case and return results as results object
    results = case.res  # the results object
    assert results is not None, "No results found"
    assert results.res is not None, "No results found"
    assert results.res.jspath(path="$.header.case", typ=str, error_msg=True) == case.name
    # default initial settings, superceeded by base case values
    x = [0, 0, x_z]  # z-value is in inch =! 1m!
    v = [1.0, 0, 0]
    # adjust to case settings:
    _spec = case.js.jspath(path="$.spec")
    assert isinstance(_spec, dict), "No spec found in case"
    for k, val in _spec.items():
        if k in ("stepSize", "stopTime"):
            pass
        elif k == "g":
            g = val
        elif k == "e":
            e = val
        elif k == "x[2]":
            x[2] = val
        elif k not in ("x@step", "v@step", "x_b@step"):
            raise KeyError(f"Unknown key {k}")
    # check correct reporting of start values: ! seems unfortunately not possible!
    # expected time and position of first bounce
    t_bounce = sqrt(2 * x[2] * hf / g)
    v_bounce = g * t_bounce  # speed in z-direction
    x_bounce = v[0] * t_bounce  # x-position where it bounces
    # check outputs after first step:
    assert results.res.jspath(path="$['0'].bb.e") == e, "??Initial value of e"
    assert results.res.jspath(path="$['0'].bb.g") == g, "??Initial value of g"
    assert results.res.jspath(path="$['0'].bb.x[2]") == x[2], "??Initial value of x[2]"
    # print("0.01", results.res.jspath(path="$['0.01']"))
    # print( results.res.jspath(path="$['0.01'].bb.x"), (dt, 0, x[2] - 0.5 * g * dt**2 / hf))

    arrays_equal(
        res=results.res.jspath(path="$['0.01'].bb.x") or (),
        expected=(dt, 0, x[2] - 0.5 * g * dt**2 / hf),
    )
    arrays_equal(
        res=results.res.jspath(path="$['0.01'].bb.v") or (),
        expected=(v[0], 0, -g * dt),
    )
    x_b = results.res.jspath(path="$.['0.01'].bb.['x_b']")
    assert isinstance(x_b, Sequence), f"Expected sequence, found {type(x_b)}"
    assert abs(x_b[0] - x_bounce) < 1e-9
    # just before bounce
    t_before = int(t_bounce * tfac) / tfac  # * dt  # just before bounce
    if t_before == t_bounce:  # at the interval border
        t_before -= dt

    arrays_equal(
        res=results.res.jspath(path=f"$['{t_before}'].bb.x") or (),
        expected=(v[0] * t_before, 0, x[2] - 0.5 * g * t_before**2 / hf),
    )
    arrays_equal(
        res=results.res.jspath(path=f"$['{t_before}'].bb.v") or (),
        expected=(v[0], 0, -g * t_before),
    )
    x_b = results.res.jspath(path=f"$['{t_before}'].bb.['x_b']")
    assert isinstance(x_b, Sequence), f"Expected sequence, found {type(x_b)}"
    assert abs(x_b[0] - x_bounce) < 1e-9
    # just after bounce
    ddt = t_before + dt - t_bounce  # time from bounce to end of step
    x_bounce2 = x_bounce + 2 * v_bounce * e * 1.0 * e / g
    arrays_equal(
        res=results.res.jspath(path=f"$['{t_before + dt}'].bb.x") or (),
        expected=(
            t_bounce * v[0] + v[0] * e * ddt,
            0,
            (v_bounce * e * ddt - 0.5 * g * ddt**2) / hf,
        ),
    )

    arrays_equal(
        res=results.res.jspath(path=f"$['{t_before + dt}'].bb.v") or (),
        expected=(e * v[0], 0, (v_bounce * e - g * ddt)),
    )
    x_b = results.res.jspath(path=f"$['{t_before + dt}'].bb.['x_b']")
    assert isinstance(x_b, Sequence), f"Expected sequence, found {type(x_b)}"
    assert abs(x_b[0] - x_bounce2) < 1e-9
    # from bounce to bounce
    v_x, v_z, t_b, x_b = (
        v[0],
        v_bounce,
        t_bounce,
        x_bounce,
    )  # set start values (first bounce)
    # print(f"1.bounce time: {t_bounce} v_x:{v_x}, v_z:{v_z}, t_b:{t_b}, x_b:{x_b}")
    for n in range(2, 100):  # from bounce to bounce
        print(f"Case {casename}. Bounce {n}")
        v_x = v_x * e  # adjusted speeds
        v_z = v_z * e
        delta_t = 2 * v_z / g  # time for one bounce (parabola): v(t) = v0 - g*t/2 => 2*v0/g = t
        t_b += delta_t
        x_b += v_x * delta_t
        _tb = int(t_b * tfac) / tfac
        if results.res.jspath(path=f"$['{_tb + dt}']") is None:
            break
        bb_x = results.res.jspath(path=f"$['{_tb}'].bb.x")
        assert isinstance(bb_x, Sequence), f"Expected sequence, found {type(bb_x)}"
        _z = bb_x[2]
        # bb_x = results.res.jspath(path=f"$['{_tb + dt}'].bb.x")
        # assert isinstance(bb_x, Sequence), f"Expected sequence, found {type(bb_x)}"
        # z_ = bb_x[2]
        bb_v = results.res.jspath(path=f"$['{_tb}'].bb.v")
        assert isinstance(bb_v, Sequence), f"Expected sequence, found {type(bb_v)}"
        _vx = bb_v[0]
        _vz = bb_v[2]
        bb_v = results.res.jspath(path=f"$['{_tb + dt}'].bb.v")
        assert isinstance(bb_v, Sequence), f"Expected sequence, found {type(bb_v)}"
        # sourcery skip: move-assign
        vx_ = bb_v[0]
        vz_ = bb_v[2]
        assert abs(_z) < x[2] * 5e-2, f"Bounce {n}@{t_b}. z-position {_z} should be close to 0 ({x[2] * 5e-2})"
        if delta_t > 2 * dt:
            assert _vz < 0, f"Bounce {n}@{t_b}. Expected speed sign change {_vz}-{vz_}when bouncing"
            assert vz_ > 0, f"Bounce {n}@{t_b}. Expected speed sign change {_vz}-{vz_}when bouncing"
            assert _vx * e == vx_, f"Bounce {n}@{t_b}. Reduced speed in x-direction. {_vx}*{e}!={vx_}"


def test_run_cases():
    path = Path(Path(__file__).parent, "data/BouncingBall3D/BouncingBall3D.cases")
    assert path.exists(), "BouncingBall3D cases file not found"
    cases = Cases(spec=path)
    check_case(
        cases=cases,
        casename="base",
        stepSize=0.01,
        stopTime=3,
        g=9.81,
        e=1.0,
        x_z=1 / 0.0254,
        hf=0.0254,
    )
    check_case(
        cases=cases,
        casename="restitution",
        stepSize=0.01,
        stopTime=3,
        g=9.81,
        e=0.5,
        x_z=1 / 0.0254,
        hf=0.0254,
    )
    check_case(
        cases=cases,
        casename="gravity",
        stepSize=0.01,
        stopTime=3,
        g=1.5,
        e=1.0,
        x_z=1 / 0.0254,
        hf=0.0254,
    )
    check_case(
        cases=cases,
        casename="restitutionAndGravity",
        stepSize=0.01,
        stopTime=3,
        g=1.5,
        e=0.5,
        x_z=1 / 0.0254,
        hf=0.0254,
    )


if __name__ == "__main__":
    retcode = pytest.main(["-rA", "-v", __file__, "--show", "True"])
    assert retcode == 0, f"Non-zero return code {retcode}"
    # import os
    # os.chdir(Path(__file__).parent.absolute() / "test_working_directory")
    # test_make_fmu()
    # test_run_fmpy( show=True)
    # test_run_cases()

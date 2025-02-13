from pytest import warns

from gym_cas import cos, solve_interval, x
from gym_cas.globals import _only_small_errors


def test_solve_interval():
    sol = solve_interval(x**2 + x * cos(x) ** 2 - 1, -10, 10)
    assert len(sol) == 2
    assert _only_small_errors(-1.10564834684030, sol[0])
    assert _only_small_errors(0.777969224724682, sol[1])

    with warns(UserWarning, match="Could not find root"):
        sol = solve_interval(x**2 + 1, -10, 10)
        assert len(sol) == 0

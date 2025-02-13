from typing import Union
from warnings import warn

from sympy import nsolve


def solve_interval(eq, start: Union[float, int], end: Union[float, int], n=100, **kwargs):
    """Løs ligning numerisk i et interval.

    Parametre
    ---
    eq : ligning
        En ligning med en ubekendt.

    start : int, float
        Start på intervallet hvor løsninger skal findes.

    end : int, float
        Slutningen på intervallet hvor løsninger skal findes.

    n : int, default = 100
        Antal gange der skal forsøges. `nsolve` kaldes n gange.

    kwargs : Se `nsolve`

    Returnerer
    ---
    solutions : list
        Liste med fundne løsninger. Er tom hvis ingen løsninger blev fundet.

    Se også
    ---
    - [SymPy: Solve One or a System of Equations Numerically](https://docs.sympy.org/latest/guides/solving/solve-numerically.html)
    """

    solutions = []
    value_error = None
    n_warn, max_warn = 0, 10
    step = (end - start) / n
    for i in range(0, n):
        x0 = start + i * step
        try:
            solution = nsolve(eq, x0, **kwargs)
            if start <= solution <= end:
                solutions.append(solution)
        except ValueError as e:
            value_error = e
        except Exception as e:
            if n_warn < max_warn:
                warn(str(e), stacklevel=2)
                n_warn += 1
    solutions = list(set(solutions))
    if len(solutions) == 0 and value_error is not None:
        warn(str(value_error), stacklevel=2)

    solutions.sort()
    return solutions

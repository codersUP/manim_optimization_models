from functools import reduce
import sympy as sp
from scipy.optimize import minimize
import numpy as np
from pprint import pprint
import json


def convert_list_to_tuples(list):
    return reduce(lambda a, b: a + (b,), list, ())


def newton(vars, func, initial_point, cycles=100, verbose=False):
    vars = convert_list_to_tuples([sp.symbols(v) for v in vars])

    func = sp.parse_expr(func)
    func_lambda = sp.Lambda(vars, func)
    func_evaluated = lambda x: np.array([func_lambda(*x)], dtype=float)

    gradient_lambda = np.array([sp.Lambda(vars, sp.diff(func, var)) for var in vars])
    gradient_evaluated = lambda x: np.array(
        [g(*x) for g in gradient_lambda], dtype=float
    )

    initial_point = np.array(initial_point, dtype=float)

    m = minimize(
        func_evaluated,
        initial_point,
        method="Newton-CG",
        jac=gradient_evaluated,
        options={"return_all": True, "maxiter": cycles},
    )

    return {
        "min": m["fun"],
        "min_value": m["x"],
        "points": m["allvecs"],
    }


def main():
    f = open("newton.json")
    data = json.load(f)

    m = newton(**data)
    min = m["min"]
    min_values = m["min_value"]

    print(min, min_values)
    pprint(m["points"])


if __name__ == "__main__":
    main()

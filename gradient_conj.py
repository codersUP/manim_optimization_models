from functools import reduce
import sympy as sp
from scipy.optimize import line_search
import numpy as np
from pprint import pprint
import json


EPSILON = 0.1


def convert_list_to_tuples(list):
    return reduce(lambda a, b: a + (b,), list, ())


def module_of_vector(vector):
    return sum(map(lambda x: x * x, vector))


def gradient_conj(vars, func, initial_point, cycles=100, verbose=False):
    vars = convert_list_to_tuples([sp.symbols(v) for v in vars])

    func = sp.parse_expr(func)
    func_lambda = sp.Lambda(vars, func)
    func_evaluated = lambda x: np.array([func_lambda(*x)], dtype=float)

    gradient_lambda = np.array([sp.Lambda(vars, sp.diff(func, var)) for var in vars])
    gradient_evaluated = lambda x: np.array(
        [g(*x) for g in gradient_lambda], dtype=float
    )

    initial_point = np.array(initial_point, dtype=float)

    points = [
        {
            "point": initial_point,
            "value": func_evaluated(initial_point),
            "iteration": 1,
            "gradient": gradient_evaluated(initial_point),
            "s": -1 * gradient_evaluated(initial_point),
            "step_arrived": 0,
        }
    ]

    if verbose:
        pprint(points[-1])

    for _ in range(cycles):
        start_point = points[-1]["point"]
        step = points[-1]["iteration"]
        search_gradient = points[-1]["s"]

        try:
            res = line_search(
                func_evaluated, gradient_evaluated, start_point, search_gradient
            )

            r_point = start_point + res[0] * search_gradient

            if module_of_vector(search_gradient) < EPSILON:
                break

            points.append(
                {
                    "point": r_point,
                    "value": func_evaluated(r_point),
                    "iteration": step + 1,
                    "gradient": gradient_evaluated(r_point),
                    "s": -1 * gradient_evaluated(r_point)
                    + search_gradient
                    * module_of_vector(gradient_evaluated(r_point))
                    / module_of_vector(gradient_evaluated(start_point)),
                    "step_arrived": res[0],
                }
            )

            if verbose:
                pprint(points[-1])

        except Exception as e:
            break

    return {
        "min": points[-1]["point"],
        "min_value": points[-1]["value"],
        "points": points,
    }


def main():
    f = open("gradient_conj.json")
    data = json.load(f)

    m = gradient_conj(**data)
    min = m["min"]
    min_values = m["min_value"]

    print(min, min_values)
    pprint(m["points"])


if __name__ == "__main__":
    main()

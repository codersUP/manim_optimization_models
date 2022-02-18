from functools import reduce
import sympy as sp
from scipy.optimize import line_search
import numpy as np
from pprint import pprint
import json


EPSILON = 0.1


def convert_list_to_tuples(list):
    return reduce(lambda a, b: a + (b,), list, ())


def gradient(vars, func, initial_point, cycles=100, verbose=False):
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
            "step_arrived": 0,
        }
    ]

    if verbose:
        pprint(points[-1])

    # start_point = points[-1]["point"]
    for _ in range(cycles):
        start_point = points[-1]["point"]
        step = points[-1]["iteration"]
        gradient = gradient_evaluated(start_point)
        search_gradient = -1 * gradient

        try:
            res = line_search(
                func_evaluated, gradient_evaluated, start_point, search_gradient
            )
            print(res[0])
            r_point = start_point + res[0] * search_gradient
            # search_gradient = res[5]
            # x_2 = [0 for _ in range(len(vars))]
            # for j in range(len(vars)):
            #     x_2[j] = r_point[j] - start_point[j]

            # if((np.linalg.norm(gradient_evaluated(r_point)) <= 0.001) or (np.linalg.norm(x_2)/np.linalg.norm(start_point)) <= 0.001):
            #     break
            
            if points[-1]["value"] - func_evaluated(r_point) < EPSILON:
                break

            points.append(
                {
                    "point": r_point,
                    "value": func_evaluated(r_point),
                    "iteration": step + 1,
                    "gradient": gradient_evaluated(r_point),
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
    f = open("gradient.json")
    data = json.load(f)

    m = gradient(**data)
    min = m["min"]
    min_values = m["min_value"]

    print(min, min_values)
    pprint(m["points"])


if __name__ == "__main__":
    main()
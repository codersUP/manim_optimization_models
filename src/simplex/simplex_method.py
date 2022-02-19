import json
import os
import numpy as np

from scipy.optimize import linprog
from .utils import parseArray, parseMatrix, message


def simplex_algorithm(data):
    results = []
    def callback_func(res):
        results.append(res)

    ans = linprog(
        data["vars_c"],
        data["A_ineq"],
        data["b_ineq"],
        data["A_eq"],
        data["b_eq"],
        bounds=data["bounds"],
        method="simplex",
        callback=callback_func
    )

    return results, ans

def call_simplex():
    inputPath = os.path.abspath(os.path.join(__file__, "../input.json"))
    with open(inputPath, 'r') as fp:
        data = json.load(fp)
    
    results, ans = simplex_algorithm(data)

    tempfile = ".temp"
    with open(tempfile, 'w') as fp:
        fp.write(message(ans))

    return data, results, ans

     # data = {
    #     "vars_c": np.array([-2, -3]),
    #     "A_ineq": np.array([[1, 1], [1, 2], [-1, 1]]),
    #     "b_ineq": np.array([3, 4, 1]),
    #     "A_eq": None,
    #     "b_eq": None,
    #     "bounds": ((0, None), (0, None)),
    # }

    # data = {
    #     "vars_c": np.array([1, 1, 4]),
    #     "A_ineq": None,
    #     "b_ineq": None,
    #     "A_eq": np.array([[1, -1, -1], [2, -3, -3]]),
    #     "b_eq": np.array([1, 2]),
    #     "bounds": ((0, None), (0, None), (0, None)),
    # }

    # data = {
    #     "vars_c": np.array([8,-2]),
    #     "A_ineq": None,
    #     "b_ineq": None,
    #     "A_eq": np.array([[1, -1], [-4, 1]]),
    #     "b_eq": np.array([1, 4]),
    #     "bounds": ((0, None), (0, None)),
    # }
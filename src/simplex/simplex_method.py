import json
import os
import numpy as np

from scipy.optimize import linprog
from .utils import message


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

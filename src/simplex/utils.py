from sympy import sympify
import numpy as np

# returns whether each element of each list is equal to the other
def equals(list1, list2):
    if len(list1) != len(list2):
        return False
    for i, item in enumerate(list1):
        if item != list2[i]:
            return False

    return True


def parseArray(list):
    if list == "" :
        return None
    result = [(float(sympify(x, convert_xor=False, evaluate=True)) if x != "" else None) for x in list]
    return result

def parseMatrix(matrix):
    if matrix == "" :
        return None
    return [parseArray(row) for row in matrix]

def transform2D(data):
    return {
        "vars_c": transformArray(data["vars_c"]),
        "A_ineq": transformMatrix2D(data["A_ineq"]),
        "b_ineq": transformArray(data["b_ineq"]),
        "A_eq": transformMatrix2D(data["A_eq"]),
        "b_eq": transformArray(data["b_eq"]),
        "bounds": data["bounds"][:2],
        "ranges": data["ranges"][:2]
    }

def transformMatrix2D(matrix):
    if matrix is None: return None
    return [item[:2] for item in matrix]

def transformArray(array):
    if array is None: return None
    return array[:2]


def message(ans):
    msg = ""
    if ans.success:
        msg += f"El algoritmo de optimización de Simplex fue exitoso.\nEl punto mínimo de la función hallado fue {ans.fun} "
        msg += f"que se obtuvo para el punto {ans.x}.\n"
    else:
        msg += "La optimización con el algoritmo Simplex no fue exitosa.\n"
        if ans.status == 2:
            msg += "El problema pudiera no tener solución factible.\n"
        elif ans.status == 3:
            msg += "El problema parece estar no acotado.\n"
    msg += f"El número total de iteraciones realizadas fueron {ans.nit}."
    return msg


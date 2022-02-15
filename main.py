import sympy as sp
from scipy.optimize import minimize
from sympy.parsing.sympy_parser import parse_expr
import numpy as np
from pprint import pprint
import json

MIN = 1e10000
EPSILON = 0.1


def check_int(x, epsilon):
    if abs(x - int(x)) < epsilon or abs(x - (int(x) + 1)) < epsilon:
        return True
    return False


def move_inequality_constants(ineq):
    l = ineq.lhs
    r = ineq.rhs
    op = ineq.rel_op

    if op == "<=":
        return sp.GreaterThan(r - l, 0)
    elif op == "<":
        return sp.StrictGreaterThan(r - l, 0)
    elif op == ">=":
        return sp.GreaterThan(l - r, 0)
    elif op == ">":
        return sp.StrictGreaterThan(l - r, 0)
    elif op == "=":
        return sp.Eq(l - r, 0)
    raise Exception("no restriction")


def func_eval(x_vector, value_vector, func):
    for x_i, v_i in zip(x_vector, value_vector):
        func = func.subs(x_i, v_i)
    return func


def c_func(vars, fun):
    return lambda values: func_eval(vars, values, fun)


def get_constraints(constraints, vars):
    g = []

    for c in constraints:
        cm = move_inequality_constants(parse_expr(c))
        op = cm.rel_op

        if op == "<=" or op == "<" or op == ">=" or op == ">":
            g.append(
                {
                    "type": "ineq",
                    "fun": c_func(vars, cm.lhs),
                }
            )
        elif op == "=":
            g.append(
                {
                    "type": "eq",
                    "fun": c_func(vars, cm.lhs),
                }
            )
    return g


def f_func(vars, func):
    return lambda values: func_eval(vars, values, parse_expr(func))


def branch_and_bound_int(vars, func, constraints, initial_point):
    vars = [sp.symbols(i) for i in vars]
    constraints = get_constraints(constraints, vars)

    min = MIN
    min_values = initial_point.copy()

    stack = [{"initial_point": initial_point.copy(), "constraints": constraints.copy()}]

    while len(stack):

        act = stack.pop()
        values = act["initial_point"]
        cons = act["constraints"]

        m = minimize(f_func(vars, func), values, constraints=cons)
        print(m)

        if m.success and m.fun < min:
            all_int = True
            for i, v in enumerate(m.x):
                if not check_int(v, EPSILON):
                    all_int = False

                    stack.append(
                        {
                            "initial_point": m.x.copy(),
                            "constraints": cons.copy()
                            + [
                                {
                                    "type": "ineq",
                                    "fun": c_func(vars, int(v) - vars[i]),
                                }
                            ],
                        }
                    )
                    stack.append(
                        {
                            "initial_point": m.x.copy(),
                            "constraints": cons.copy()
                            + [
                                {
                                    "type": "ineq",
                                    "fun": c_func(vars, vars[i] - (int(v) + 1)),
                                }
                            ],
                        }
                    )
            if all_int:
                min = m.fun
                min_values = m.x

    print(min, min_values)


def main():
    f = open("bab.json")
    data = json.load(f)

    branch_and_bound_int(**data)


if __name__ == "__main__":
    main()

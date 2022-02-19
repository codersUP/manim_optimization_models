import json
from functools import reduce
import sympy as sym
import os
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, convert_equals_signs
def move_inequality_constants(ineq):
    l = ineq.lhs
    r = ineq.rhs
    op = ineq.rel_op    
    
    if op.__contains__('>'):
        return l - r
    else: 
        return r - l
    
def func_eval(x_vector, value_vector, func):
    f = func
    for x_i, v_i in zip(x_vector, value_vector):
        f = f.subs(x_i, v_i)
    return f

def get_lambda(x_vector, f):
    return sym.Lambda(('x', 'y'), f)

def get_constraints(constraints):
    result = list()
    for c in constraints:
        result.append((move_inequality_constants(parse_expr(c))))
    return result

def get_evaluated_constraints(variables, values, constraints):
    result = list()
    for con in constraints:
        result.append(func_eval(variables, values, con))
    return result

def read_json(path):
    with open(path) as settings:
        data = json.load(settings)

    f = data['Penalty_func']
    variables = data['Penalty_vars']
    c = data['Penalty_constraints']
    
    constraints = get_constraints(c)
    function = parse_expr(f)
    
    return variables, function, constraints

def convert_list_to_tuples(list):
    return reduce(lambda a, b: a + (b,), list, ())

def save_process(my_dict):
    
    inputPath = os.path.abspath(os.path.join(__file__, "../data.json"))
    with open(inputPath, 'r') as fp1:
        data = json.load(fp1)
    for key in my_dict.keys():
        data[key] = my_dict[key]
    with open(inputPath, 'w') as fp:
        json.dump(data, fp)

def load_saved_data(key):   
    inputPath = os.path.abspath(os.path.join(__file__, "../data.json"))
    with open(inputPath, 'r') as fp:
        data = json.load(fp)
    try:
        return data[key]
    except KeyError:
        return None

def get_key_name(func, constraints):
    f = str(func) + ' '
    for i, c in enumerate(constraints):
        f+= str(c) + ' ' if i != len(constraints) else str(c)
    return f


x = sym.Symbol('x')
y = sym.Symbol('y')
# def get_min_cleared_constraint(ineq):
#     l = ineq.lhs
#     r = ineq.rhs
#     if len(l.free_symbols) == 2:
#         # estan ambas dos en la izquierda aún
#         newr = r
#         for arg in l.args:
#             if arg.free_symbols.__contains__(y):
#                 newl = arg
#                 continue
#             if l.is_Add:
#                 newr -= arg
#             elif l.is_Mul:
#                 newr /= arg
#         return get_min_cleared_constraint(newl >= newr)
#     if len(l.free_symbols) == 1:
#         if l.free_symbols.__contains__(y):
#             if len(l.args) == 0:
#                 return ineq
#             else:
#                 newr = r
#                 for arg in l.args:
#                     if arg.free_symbols.__contains__(y):
#                         newl = arg
#                         continue
#                     if l.is_Add:
#                         newr -= arg
#                     elif l.is_Mul:
#                         newr /= arg
#             return get_min_cleared_constraint(newl >= newr)
#         elif l.free_symbols.__contains__(x):
#             if len(l.args) == 0:
#                 return ineq
#             else:
#                 newr = r
#                 for arg in l.args:
#                     if arg.free_symbols.__contains__(x):
#                         newl = arg
#                         continue
#                     if l.is_Add:
#                         newr -= arg
#                     elif l.is_Mul:
#                         newr /= arg
#                 return get_min_cleared_constraint(newl >= newr)
    # if ineq.rel_op.__contains__('>'):
    #     return newl >= newr
    # else: 
    #     return newl <= newr
    
# x**2 = 4 => x = log4_2

def get_cleared_constraint(ineq):
    if len(ineq.free_symbols) >= 2:
        if ineq.free_symbols.__contains__(y):
            a = sym.solve(ineq, y)
            return a.args[1]
        else:
            a = sym.solve(ineq, x)
            return a.args[1]
    else:
        if ineq.free_symbols.__contains__(y):
            a = sym.solve(ineq, y)
            return a.args[0]
        else:
            a = sym.solve(ineq, x)
            return a.args[0]
def get_eq_cleared_constraint(ineq):
    if len(ineq.free_symbols) >= 2:
        if ineq.free_symbols.__contains__(y):
            a = sym.solve(ineq, y)
            return a[0], y
        else:
            a = sym.solve(ineq, x)
            return a[0], x
    else:
        if ineq.free_symbols.__contains__(y):
            a = sym.solve(ineq, y)
            return a[0], y
        else:
            a = sym.solve(ineq, x)
            return a[0], x

def move_inequality_to_min(ineq):
    l = ineq.lhs
    r = ineq.rhs
    op = ineq.rel_op    
    
    if op.__contains__('>'):
        return ineq
    else: 
        return -1*l >= -1*r
def move_inequality_to_max(ineq):
    l = ineq.lhs
    r = ineq.rhs
    op = ineq.rel_op    
    
    if op.__contains__('<'):
        return ineq
    else: 
        return -1*l <= -1*r
    
def get_constraints_cleared(ineqs_, max_or_min=0):
    ineqs = [get_cleared_constraint(ineq) for ineq in ineqs_]
    return ineqs
def get_lambdas(ineqs):
    lam = []
    for i in ineqs:
        l = i.lhs
        r = i.rhs
        if len (l.free_symbols) == 1:
            syms = [s for s in r.free_symbols]
            if len(syms) == 0:
                syms = [x] if r.free_symbols.__contains__(y) else [y]
            lam.append(sym.Lambda(syms, r))
        elif len (l.free_symbols)  == 0:
            syms = [x] if r.free_symbols.__contains__(y) else [y]
            lam.append(sym.Lambda(syms, l))
        else:
            syms = [s for s in l.free_symbols]
            lam.append(sym.Lambda(syms, l))
    return lam
def get_eq(ineqs):
    lam = []
    for i in ineqs:
        l = i.lhs
        r = i.rhs
        if len (l.free_symbols) == 1:
            lam.append(r)
        else:
            lam.append(l)
    return lam

def check_constraint_point(x_, y_, constraints_, lambdas_):
    for c, l in zip(constraints_,lambdas_):
        op = c[1]
        _y = l(x_)
        if op.__contains__('>') and y_ < _y:
            return False
        elif op.__contains__('<') and y_ > _y:
            return False
    return True
def check_eq_constraint_point(x_, y_, lambdas_):
    for l in lambdas_:
        _y = l(x_)
        if _y != y_:
            return False
    return True

################## geometric ###################
def get_geometric_ineqs_and_eqs(constraints):
    ineqs = []
    eqs = []
    for c in constraints:
        con = parse_expr(c, transformations = standard_transformations+(convert_equals_signs,))
        l = con.lhs
        r = con.rhs
        op = con.rel_op
    
        if op == "<=":
            ineqs.append(con)
        elif op == "<":
            ineqs.append(con)
        elif op == ">=":
            ineqs.append(con)
        elif op == ">":
            ineqs.append(con)
        elif op == "==":
            eqs.append(con)
    return ineqs, eqs

################### penalty ######################
def get_penalty_ineqs_and_eqs(constraints):
    ineqs = []
    eqs = []
    for c in constraints:
        con = parse_expr(c, transformations = standard_transformations+(convert_equals_signs,))
        l = con.lhs
        r = con.rhs
        op = con.rel_op
    
        if op == "<=":
            ineqs.append(con)
        elif op == "<":
            ineqs.append(con)
        elif op == ">=":
            ineqs.append(con)
        elif op == ">":
            ineqs.append(con)
        elif op == "==":
            eqs.append(con)
    return ineqs, eqs
    
def get_penalty_eq_constraints(eqs):
    if len(eqs) == 0:
        return [], None
    result = list()
    total_eq = eqs[0]
    result.append(total_eq.lhs-total_eq.rhs)
    total_eq = (result[0])**2
    for eq in eqs[1:]:
        parsed_eq = eq
        result.append(parsed_eq.lhs-parsed_eq.rhs)
        total_eq += (parsed_eq.lhs-parsed_eq.rhs)**2
    return result, total_eq

################### penalty for minimize
def move_inequality_constants_minimize(ineq):
    l = ineq.lhs
    r = ineq.rhs
    op = ineq.rel_op    

    if op.__contains__('>'):
        return l - r
    else: 
        return r - l


def get_penalty_ineq_constraints_minimize(ineqs):
    if len(ineqs) == 0:
        return [], None
    result = list()
    total_ineq = move_inequality_constants_minimize(ineqs[0])
    result.append(total_ineq)
    total_ineq = (sym.Max(0, total_ineq))**2
    for c in ineqs[1:]:
        ineq = move_inequality_constants_minimize(c)
        result.append(ineq)
        total_ineq += (sym.Max(0, ineq))**2
    return result, total_ineq

def get_penalty_func_minimize(func, ineqs, eqs, variables, step):
    penalty_func = func = parse_expr(func)
    parsed_eqs, eqs_func = get_penalty_eq_constraints(eqs)
    parsed_ineqs, ineqs_func = get_penalty_ineq_constraints_minimize(ineqs)
    penalty_func = penalty_func + step * eqs_func if eqs_func is not None else penalty_func
    penalty_func = penalty_func + step * ineqs_func if ineqs_func is not None else penalty_func
    penalty_lambda = sym.Lambda((variables[0], variables[1]), penalty_func)
    return func, penalty_func, penalty_lambda, parsed_eqs, parsed_ineqs

################### penalty for maximize
def move_inequality_constants_maximize(ineq):
    l = ineq.lhs
    r = ineq.rhs
    op = ineq.rel_op    
    
    if op.__contains__('<'):
        return l - r
    else: 
        return r - l
    
def get_penalty_ineq_constraints_maximize(ineqs):
    if len(ineqs) == 0:
        return [], None
    result = list()
    total_ineq = move_inequality_constants_maximize(ineqs[0])
    result.append(total_ineq)
    total_ineq = sym.Max(0, total_ineq)
    for c in ineqs[1:]:
        result.append((move_inequality_constants_maximize(c)))
        total_ineq += sym.Max(0, move_inequality_constants_maximize(c))
    return result, total_ineq

def get_penalty_func_maximize(func, ineqs, eqs, variables, step):
    penalty_func = func = parse_expr(func)
    parsed_eqs, eqs_func = get_penalty_eq_constraints(eqs)
    parsed_ineqs, ineqs_func = get_penalty_ineq_constraints_maximize(ineqs)
    penalty_func = penalty_func + step * eqs_func if eqs_func is not None else penalty_func
    penalty_func = penalty_func + step * ineqs_func if ineqs_func is not None else penalty_func
    penalty_lambda = sym.Lambda((variables[0], variables[1]), penalty_func)
    return func, penalty_func, penalty_lambda, parsed_eqs, parsed_ineqs

#################################################################
# 0 for minimize, 1 for maximize
def get_penalty_func(func, constraints, variables, step, max_or_min = 0):
    ineqs, eqs = get_penalty_ineqs_and_eqs(constraints)
    if max_or_min == 0: # minimize
        return ineqs, *get_penalty_func_minimize(func, ineqs, eqs, variables, step)
    else: # maximize
        return ineqs, *get_penalty_func_maximize(func, ineqs, eqs, variables, step)

def read_dots_from_json(string_):
    dots = []
    splited_text = (string_[2:len(string_)-2].split('['))
    for splited in splited_text[:len(splited_text)-1]:
        new_splited = splited.split(', ')
        dots.append((float(new_splited[0]), float(new_splited[1][:len(new_splited[1])-1])))
        a = 0
    last_row = splited_text[-1].split(', ')
    dots.append((float(last_row[0]), float(last_row[1])))
    return dots
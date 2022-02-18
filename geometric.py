import numpy as np
from shapely.geometry import LineString
from sympy.parsing.sympy_parser import parse_expr
import sympy as sym
from utils import *

def geometric_aproach(ineqs, equation, x1, y1, min_max = 0):
    equation = sym.Lambda(('x', 'y'), equation)
    ineqs_, eqs_ = get_geometric_ineqs_and_eqs(ineqs)
    converted = get_constraints_cleared(ineqs_)
    eq_converted = [get_eq_cleared_constraint(eq_)for eq_ in eqs_]
    x_constraints = []
    y_constraints = []
    for c in converted:
        l = c.lhs
        r = c.rhs
        op = c.rel_op
        if len (l.free_symbols) == 1:
            if l.free_symbols.__contains__(x):
                x_constraints.append([c, op])
            else:
                y_constraints.append([c, op])
        elif len (r.free_symbols) == 1:
            op = '<=' if op.__contains__('>') else '>='
            if r.free_symbols.__contains__(x):
                x_constraints.append([c, op])
            else:
                y_constraints.append([c, op])

    lambdas_x = get_lambdas([i[0] for i in x_constraints])
    lambdas_y = get_lambdas([i[0] for i in y_constraints])
    lambdas_x_eq = []
    lambdas_y_eq = []
    for (eq_, symbol) in eq_converted:
        if symbol == sym.Symbol('x'):
            lambdas_x_eq.append(sym.Lambda(eq_.free_symbols, eq_))
        else:
            lambdas_y_eq.append(sym.Lambda(eq_.free_symbols, eq_))
            
    pairs = []
    for lam in lambdas_y:
        pairs.append((x1, [lam(i) for i in x1]))

    for lam in lambdas_x:
        pairs.append(([lam(i)for i in y1], y1))
        
    for lam in lambdas_y_eq:
        pairs.append((x1, [lam(i) for i in x1]))

    for lam in lambdas_x_eq:
        pairs.append(([lam(i)for i in y1], y1))


    lines = []
    for pair in pairs:
        lines.append(LineString(np.column_stack(pair)))

    # aqui se plotearian las líneas en manim
    # for l, (p_x, p_y) in zip(lines, pairs):
    #     plt.plot(p_x, p_y, '-', linewidth=2, color='k')


    intersections = []
    for i in range(len(lines)):
        j = i+1
        while j < len(lines):
            (i_x_, i_y_) = (lines[i].intersection(lines[j])).xy
            if len(i_x_) != 0 and check_constraint_point(i_x_[0],i_y_[0], y_constraints, lambdas_y) and check_constraint_point(i_y_[0], i_x_[0], x_constraints, lambdas_x):
                if check_eq_constraint_point(i_x_[0],i_y_[0], lambdas_y_eq) and check_eq_constraint_point(i_y_[0],i_x_[0], lambdas_x_eq):
                    intersections.append((i_x_[0],i_y_[0]))
            j+=1
    intersections.sort()
    
    # aqui se pintarian los puntos intercepción
    # for intersection in intersections:
    #     plt.plot(*intersection, 'o', color='r')

    intersects_evals = []
    for intersection in intersections:
        (int_x, int_y) = intersection 
        intersects_evals.append(round(equation(int_x, int_y), 2))
    intersects_evals.sort()

    dict1 = {}
    for i in range(len(intersects_evals)):
        dict1[i] = intersects_evals[i]
    if len(intersections) >= 1:
        #varia según min o max
        # Z = intersects_evals[-1] if min_max == 1 else intersects_evals[0]
        Zmax = intersects_evals[-1]
        Zmin = intersects_evals[0]

        m = [xi[0] for xi in intersections]
        n = [yi[1] for yi in intersections]

        # rellenar el polígono

        # posicion = max(dict1, key=dict1.get) if min_max == 1 else min(dict1, key=dict1.get)
        posicionMax = max(dict1, key=dict1.get)
        posicionMin = min(dict1, key=dict1.get)

        Xmax = m[posicionMax]
        Xmin = m[posicionMin]
        Ymax = n[posicionMax]
        Ymin = n[posicionMin]

        intersects_evals = [round(i.num, 2) for i in intersects_evals]
        Zmax = round(Zmax.num, 2)
        Zmin = round(Zmin.num, 2)

        return (pairs, lines, m, n, intersections, intersects_evals, Xmax, Ymax, Zmax, Xmin, Ymin, Zmin)
    else:
        return (pairs, lines, [], [], intersections, [], None, None, None, None, None, None)
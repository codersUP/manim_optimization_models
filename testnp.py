import json
import sympy as sym
from sympy.parsing.sympy_parser import parse_expr

g = list()
# x = list()
# x.append("x0")
# for i in range(1,20):
#     q="x"+str(i)
#     x.append(sym.Symbol(q))
# print(x)

# f='x**2+2y+1'#input("f(x)=x**2+x")
# f=parse_expr(f)
# print(f.subs('x', 2))
def move_inequality_constants(ineq):
    l = ineq.lhs
    r = ineq.rhs
    op = ineq.rel_op    
    
    if op.__contains__('<'):
        return l - r
    else: 
        return r - l
def func_eval(x_vector, value_vector, func):
    f = func
    for x_i, v_i in zip(x_vector, value_vector):
        f = f.subs(x_i, v_i)
    return f
# f1 = lambda x,y: x**2+y+1
# print(f1(1,2))
with open('settings.json') as settings:
    data = json.load(settings)

x = data['vars']
f = data['func']
constraints = data['constraints']

c = parse_expr(constraints[0])
c = move_inequality_constants(c)
print(c)

f = parse_expr(f)
values = [2,2]

print(func_eval(x, values, f))

gfg = sym.Lambda(x, f)
print(gfg(2,2))

def get_constraints(constraints):
    g = list()
    for c in constraints:
        g.append((move_inequality_constants(parse_expr(c))))


# def multi_f(x_vector):
#     with open('settings.json') as settings:
#         data = json.load(settings)

#     x = data['vars']
#     f = data['func']
#     constraints = data['constraints']
#     c = parse_expr(constraints[0])
#     c = move_inequality_constants(c)
#     function = parse_expr(f)
#     sum_ = func_eval(x_vector, values, function)
# 	# sum_ = pow((pow(x[0],2) + x[1] - 11),2) + pow((pow(x[1],2) + x[0] - 7),2)
# 	g[0] = -26.0 + pow((x[0]-5.0), 2) + pow(x[1],2)#constraints.

# 	for i in range(nc):
# 		if(g[i] < 0.0): ## meaning that the constraint is violated.
# 			sum_ = sum_ + r*g[i]*g[i]

# 	return(sum_)
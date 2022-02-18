

# from scipy.optimize import minimize, line_search
# import sympy as sym
# from sympy.parsing.sympy_parser import parse_expr, standard_transformations, convert_equals_signs
# from utils import func_eval, get_lambdas, get_constraints_cleared, get_penalty_func, get_penalty_ineq_constraints_minimize, get_eq, get_penalty_eq_constraints
# import numpy as np
# from gradient import gradient
# # rz = lambda x: (1-x[0])**2 + 100*(x[1] - x[0]**2)**2
# # h_1 = lambda x: (x[0] - 2 * x[1] + 2)
# # h_2 = lambda x: (-x[0] - 2 * x[1] + 6)
# # h_3 = lambda x: (-x[0] + 2 * x[1] + 2)

# # x0 = [2.3, 5]
# # cons = ({'type': 'ineq', 'fun': h_1},
# #         {'type': 'ineq', 'fun': h_2},
# #         {'type': 'ineq', 'fun': h_3}) 
# # minimize(rz, x0, constraints=cons)

# # x = sym.Symbol('x')
# # y = sym.Symbol('y')

# ineqs_ = []
# eqs_ = []
# # ineqs_.append('20*x+50*y <= 3000')
# # ineqs_.append('x - 2 * y + 2 >= 0')
# # ineqs_.append('-x - 2 * y + 6 >= 0')
# # ineqs_.append('-x + 2 * y + 2 >= 0')
# # # eqs_.append('2 = x + y')#, transformations = standard_transformations+(convert_equals_signs,)))
# # # eqs_.append('2 = x + y')#, transformations = standard_transformations+(convert_equals_signs,)))
# # func = '(1-x)**2+100*(y-x**2)**2'
# ineqs_.append('(x-5)**2+y**2-26>=0')
# func = '(x**2+y-11)**2+(x+y**2-7)**2'
# # a = parse_expr(func)
# # x = ['x']
# # la = lambda x: func_eval(['x', 'y'], [x[0], x[1]], a).p/func_eval(['x', 'y'], [x[0], x[1]], a).q
# # b = sym.Lambda(x, a)
# # c = la([2, 3])
# # d = 0
# # la funcion get_penalty_func recibe en strings:
# # la funcion objetivo, las restricciones, una tupla con las variables, 
# # el parametro de penalización y 0 o 1 para minimizar y maximizar respectivamente
# # Devuelve:
# # las inecuaciones
# # la funcion en formato sympy, la funcion de penalizacion en formato de sympy,
# # la funcion de penalización en formato lambda, las inecuaciones y las ecuaciones


# def penalty(x_, iters, epsilon_, mm = 0):
#     global func, ineqs_, eqs_
#     x_c = initial_point = [0.11, 0.1]
    
#     c = 1
#     while c < 1000:
#         ineqs, func_,  penalty_func, penalty_lambda, eqs, parsed_ineqs = get_penalty_func(func, ineqs_+eqs_, x_, c, mm)#('x', 'y'), c, mm)
#         fp = lambda x: penalty_lambda(x[0], x[1])#float(func_eval(x_, [x[0], x[1]], penalty_func))#.p/func_eval(x_, [x[0], x[1]], penalty_func).q
        
#         m = gradient(x_, str(penalty_func), x_c)
#         min_ = m["min"]
#         min_values = m["min_value"]
#         # x_1 = minimize(fp, x_c).x
#         x_1 = min_
#         print(x_1)
#         track = np.linalg.norm(x_1)/np.linalg.norm(x_c)
#         x_c = [x_1[0], x_1[1]]
#         if track <= 0.001:
#             break
#         c*= 2
#     return x_c

# x_c_ = penalty(['x', 'y'],0,0,0)

# #3.00000001176746
# #1.9999999751723971
# #0.83187365686818, 2.932764818735715
# a = 0
# # ineqs = get_penalty_eq_constraints(eqs)
# # converted = get_constraints_cleared(ineqs)
# # eq = get_eq(converted)
# # total_ineq = eq[0]
# # for e in eq[1:]:
# #     total_ineq += e
# # total_ineq += 0
# # x_constraints = []
# # y_constraints = []
# # for c in converted:
# #     l = c.lhs
# #     r = c.rhs
# #     op = c.rel_op
# #     if len (l.free_symbols) == 1:
# #         if l.free_symbols.__contains__(x):
# #             x_constraints.append([c, op])
# #         else:
# #             y_constraints.append([c, op])
# #     elif len (r.free_symbols) == 1:
# #         op = '<=' if op.__contains__('>') else '>='
# #         if r.free_symbols.__contains__(x):
# #             x_constraints.append([c, op])
# #         else:
# #             y_constraints.append([c, op])

# # lambdas_x = get_lambdas([i[0] for i in x_constraints])
# # lambdas_y = get_lambdas([i[0] for i in y_constraints])

# # hasta aqui todo en talla


# # x_c = [2.3, 3]
# # i = 1
# # while i < 1000:
# #     curr_func = lambda x: rz(x) + i*(h_1(x)**2 + h_2(x)**2 + h_3(x)**2)
# #     x_c = minimize(curr_func, x_c).x
# #     i  *= 1.2
# # print(x_c.x)

# # def eval_eq_constraints(eq, c, x_, vars_):
# #     return c * (func_eval(vars_, x_, eq))**2

# # def eval_ineq_constraints(ineq, c, x_, vars_):
# #     return c * (max(0, func_eval(vars_, x_, ineq)))**2

# # def eval_(equation, eq_cons, ineq_cons, x_, vars_, c):
# #     valor = 0
# #     for con in eq_cons:
# #         valor+= eval_eq_constraints(con, c, x_, vars_)
        
# #     for con in ineq_cons:
# #         valor+= eval_ineq_constraints(con, c, x_, vars_)
    
# #     valor+= func_eval(vars_, x_, equation)
# #     return valor


# if __name__ == "__main__":
#     func_key_name = get_key_name(function, constraints)
#     # x_ip = np.array([0.11, 0.1])
#     x_ip = np.array([2.3, 3])
#     M = 2 ## Specifies the total dimension we are working with.. //Global Var.
#     c = 1.55 ##factor for updating r.
#     numseq = 20 ## number of sequences for penalty function method.
#     r = 0.1
#     grad = np.zeros(M)
#     sol = np.zeros(M)
#     sol_ = []
#     x_2 = np.zeros(M)
# 	## has the principal values in the key name.
#     func_key_name += ' ('+str(x_ip)[1:len(str(x_ip))-1]+') '+str(numseq)+' '+str(r)+' '+str(c)
#     dic = load_saved_data(func_key_name)
#     if dic is None:
        
#         ## BRACKET OPERATOR PENALTY METHOD..1.1,1.1
#         for k in range(numseq):
#             print('\n')
#             print('sequence number ', k)
#             print('current function value is ', multi_f(x_ip))
#             x_1 = np.copy(x_ip)
#             m = newton(_variables, str(penalty_func), x_ip)
#             sol = m["min"]
#             min_values = m["min_value"]
#             # sol = DFP(x_ip)
#             x_ip = np.copy(x_1)
            
#             for j in range(M):
#                 x_2[j] = sol[j] - x_ip[j]
#             track = np.linalg.norm(x_2)/np.linalg.norm(x_ip)
#             sol_ = []
#             for i in range(M):
#                 print(sol[i])
#                 sol_.append(sol[i])
#                 x_ip[i] = sol[i]
#             sol_points.append(sol_)
#             r*= c
#             if track <= 0.001:
#                 break
#         sol_.append(func_eval(variables, sol_, function))
#         dic = {
#             func_key_name:	{
# 				'iterations': k,
# 				'points': str(sol_points),
# 				'min': str(sol_),
# 			}
#             }
#         save_process(dic)
#     else:
#         dic = load_saved_data(func_key_name)
#         print('\n')
#         print('sequence number ', dic['iterations'])
#         print('the sequence of points was ', '\n['.join(dic['points'][1:len(dic['points'])-1].split('['))+'\n')
#         print('the final solution was ', dic['min'])
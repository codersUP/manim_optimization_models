## Penalty Function method using gradient.
## Loading the libraries.
from gradient import gradient
from utils import *
import numpy as np


# Devuelve el valor de la función penalizada Φ(x, u) en un punto 

def penalty_gradient():
    with open('penalty_settings.json') as settings:
        data = json.load(settings)
    numseq      = data['Penalty_number_of_sequence']
    r           = data['Penalty_penalty_factor']
    c           = data['Penalty_update_factor']
    constraints = data['Penalty_constraints']
    min_or_max  = data['Penalty_max_or_min']
    x_ip        = data['Penalty_init_point']
    function    = data['Penalty_func']
    variables   = data['Penalty_vars']

    variables   = convert_list_to_tuples(variables)
    M = len(variables) ## Specifies the total dimension we are working with.. //Global Var.
    sol = np.zeros(M)
    x_2 = np.zeros(M)
    penalty_func = ''
    sol_ = []
    sol_points = []
    
    if min_or_max == 1:
        function = '-('+function+')'

    func_key_name = get_key_name(function, constraints)
	## has the principal values in the key name.
    func_key_name += ' ('+str(x_ip)[1:len(str(x_ip))-1]+') '+str(numseq)+' '+str(r)+' '+str(c)
    dic = load_saved_data(func_key_name)
    
    if dic is None:
        for k in range(numseq):
            print('\n')
            print('sequence number ', k)
            # gets the function, penalty_ function in sympy and the lambda of the penalty function
            _, func,  penalty_func, penalty_lambda, _, _ = get_penalty_func(function, constraints, variables, r, min_or_max)
            # gets the current point value in penalty function
            sum_ = penalty_lambda(*x_ip)
            print('current function value is ', sum_)
            x_1 = np.copy(x_ip)
            # get new approximation point
            m = gradient(variables, str(penalty_func), x_ip)
            sol = m["min"]
            x_ip = np.copy(x_1)
            
            for j in range(M):
                x_2[j] = sol[j] - x_ip[j]
                
            track = np.linalg.norm(x_2)/np.linalg.norm(x_ip)
            sol_ = []
            
            for i in range(M):
                print(sol[i])
                sol_.append(sol[i])
                x_ip[i] = sol[i]
                
            sol_points.append(sol_)
            r*= c
            # verify stop case
            if track <= 0.001:
                break
            
        sol_.append(func_eval(variables, sol_, func))
        # save info
        dic = {
            func_key_name:	{
				'iterations': k,
				'points': str(sol_points),
				'min': str(sol_),
			}
            }
        save_process(dic)
        return dic
    else:
        # in case already have been done
        dic = load_saved_data(func_key_name)
        print('\n')
        print('sequence number ', dic['iterations'])
        print('the sequence of points was ', '\n['.join(dic['points'][1:len(dic['points'])-1].split('['))+'\n')
        print('the final solution was ', dic['min'])
        return dic
    
# dict_ = penalty_gradient()
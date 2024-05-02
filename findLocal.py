from scipy.optimize import minimize
import numpy as np

def find_local(X, Y, Z, L, method, constraints : bool = False, funMethod : str = 'square', x0 : list = [42, -14, 1.4, 5.72]):
    if funMethod == 'abs':
        fun = lambda x: sum(abs((((X[i] - x[0])**2 + (Y[i] - x[1])**2 + (Z[i] - x[2])**2)**0.5 - (L[i] + x[3]))) for i in range(1, len(X)))
    elif funMethod == 'square':
        fun = lambda x: sum((((X[i] - x[0])**2 + (Y[i] - x[1])**2 + (Z[i] - x[2])**2)**0.5 - (L[i] + x[3]))**2 for i in range(1, len(X)))
        
    cons = ({'type': 'ineq', 'fun': lambda x: x[0] + 100},
            {'type': 'ineq', 'fun': lambda x: -x[0] + 100},
            {'type': 'ineq', 'fun': lambda x: x[1] + 100},
            {'type': 'ineq', 'fun': lambda x: -x[1] + 100},
            {'type': 'ineq', 'fun': lambda x: x[2] + 0},
            {'type': 'ineq', 'fun': lambda x: -x[2] + 10},
            {'type': 'ineq', 'fun': lambda x: x[3] + 100}, 
            {'type': 'ineq', 'fun': lambda x: -x[3] + 500}
        )

    if constraints == False:
        cons = ()

    x0 = np.array(x0)
    if method == 'SLSQP':
        res = minimize(fun, x0, method='SLSQP', constraints=cons)
    elif method == "BFGS":
        res = minimize(fun, x0, method='BFGS')

    print("最小值:", res.fun)
    print("最优解:", res.x)
    print('经度' + str(res.x[0] / 97.304 + 110.241))
    print('纬度' + str(res.x[1] / 111.263 + 27.204))
    print('高度' + str(res.x[2]))
    print('时间' + str(res.x[3] / 0.34))
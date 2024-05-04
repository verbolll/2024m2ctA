# findLocal.py  
# 找出音爆时的位置与时间 
from scipy.optimize import minimize
import numpy as np
import alltime

def find_local(X, Y, Z, method="SLSQP", file=None, L=None, constraints : bool = False, funMethod : str = 'square', x0 : list = [42, -14, 1.4, 5.72], ifprint : bool = True, filename = 'localData.csv'):
    with open(filename, 'a+', encoding='utf-8') as fp:
        if file != None:
            dataNumber = len(alltime.all_time(file))
            print(dataNumber)
        else:
            dataNumber = 1

        for ilenth in range(dataNumber):
            if file != None:
                L = alltime.all_time(file)[ilenth]
            if funMethod == 'abs':
                fun = lambda x: sum(abs((((X[i] - x[0])**2 + (Y[i] - x[1])**2 + (Z[i] - x[2])**2)**0.5 - (L[i] + x[3]))) for i in range(1, len(X)))
            elif funMethod == 'square':
                fun = lambda x: sum((((X[i] - x[0])**2 + (Y[i] - x[1])**2 + (Z[i] - x[2])**2)**0.5 - (L[i] + x[3]))**2 for i in range(1, len(X)))
            cons = ({'type': 'ineq', 'fun': lambda x: x[0] + 100},
                    {'type': 'ineq', 'fun': lambda x: -x[0] + 100},
                    {'type': 'ineq', 'fun': lambda x: x[1] + 100},
                    {'type': 'ineq', 'fun': lambda x: -x[1] + 100},
                    {'type': 'ineq', 'fun': lambda x: x[2] + 0},
                    {'type': 'ineq', 'fun': lambda x: -x[2] + 20},
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
            if ifprint == True:
                print("最小值:", res.fun)
                print("最优解:", res.x)
                print('经度' + str(res.x[0] / 97.304 + 110.241))
                print('纬度' + str(res.x[1] / 111.263 + 27.204))
                print('高度' + str(res.x[2]))
                print('时间' + str(res.x[3] / 0.34))
            if res.success:
                fp.write(str((res.x).tolist())[1:-2])
                fp.write('\n')
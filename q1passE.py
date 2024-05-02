from scipy.optimize import minimize
import numpy as np

X = [None, 0, 52.44686, 45.83018, 0.97304, 21.9907, -18.887]
Y = [None, 0, 28.03828, 64.6438, 69.09432, 79.77557, -9.23483]
Z = [None, 0.824, 0.727, 0.742, 0.85, 0.678, 0.575]
L = [None, 34.26078, 38.1548, 63.9268, 88.0549, 90.73614, 55.42816]

fun = lambda x: sum(abs((((X[i] - x[0])**2 + (Y[i] - x[1])**2 + (Z[i] - x[2])**2)**0.5 - (L[i] + x[3]))) for i in range(1, 7))
cons = ({'type': 'ineq', 'fun': lambda x: x[0] + 100},
        {'type': 'ineq', 'fun': lambda x: -x[0] + 100},
        {'type': 'ineq', 'fun': lambda x: x[1] + 100},
        {'type': 'ineq', 'fun': lambda x: -x[1] + 100},
        {'type': 'ineq', 'fun': lambda x: x[2] + 0},
        {'type': 'ineq', 'fun': lambda x: -x[2] + 10},
        {'type': 'ineq', 'fun': lambda x: x[3] + 100}, 
        {'type': 'ineq', 'fun': lambda x: -x[3] + 500}
       )

x0 = np.array([42, -14, 1.4, 5.72])
res = minimize(fun, x0, method='SLSQP', constraints=cons)
print(res.fun)
print(res.x)
print("最小值:", res.fun)
print("最优解:", res.x)
print('经度' + str(res.x[0] / 97.304 + 110.241))
print('纬度' + str(res.x[1] / 111.263 + 27.204))
print('高度' + str(res.x[2]))
print('时间' + str(res.x[3] / 0.34))
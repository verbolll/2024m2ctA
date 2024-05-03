# q1.py
# 第一问找出音爆点位置
import findLocal

X = [None, 0, 52.44686, 45.83018, 0.97304, 27.53703, 21.9907, -18.887]
Y = [None, 0, 28.03828, 64.6438, 69.09432, 45.95162, 79.77557, -9.23483]
Z = [None, 0.824, 0.727, 0.742, 0.85, 0.786,0.678, 0.575]
L = [None, 34.26078, 38.1548, 63.9268, 88.0549, 40.27062, 90.73614, 55.42816]

print('七个监测站')
findLocal.find_local(X, Y, Z, L=L, method='SLSQP', funMethod='abs', constraints=True, x0=[41, -14, 5.5, 1])
for i in [X, Y, Z, L]:
    i.pop(-3)
print('\n去除误差较大的检测塔E')
findLocal.find_local(X, Y, Z, L=L, method='SLSQP', funMethod='abs', constraints=True)

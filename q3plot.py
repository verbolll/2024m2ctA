# q3plot.py
# 依次画出监测塔与四次音爆的三维图
import drawpic
import numpy as np

# 以A检测塔为原点
X = [None, 0, 52.73877, 50.69538, 0.97304, 27.53703, 21.9907, -18.87698]
Y = [None, 0, 28.03828, 64.6438, 91.34692, 45.95162, 97.57765, 35.27037]
Z = [None, 0.824, 0.727, 0.742, 0.85, 0.786, 0.678, 0.575]

# 求得的各音爆时间组合
L1time = np.array([100.767, 112.22, 188.02, 258.985, 118.443, 266.871, 163.024])
L2time = np.array([164.229, 169.362, 156.936, 141.409, 86.216, 166.27, 103.738])
L3time = np.array([214.85, 92.453, 75.56, 196.517, 78.6, 175.482, 210.306])
L4time = np.array([270.065, 196.583, 110.696, 94.653, 126.669, 67.274, 206.789])

# 求得的各音爆相对检测塔A的坐标
point1 = (25.201879, 11.7936807, 12.513927)
point2 = (5.741, 49.6232, 11.4796)
point3 = (44.662257, 49.62316,13.46793)
point4 = (25.20158745, 83.00192217, 11.52885)
drawpic.drawpic(X, Y, Z, point=point1, Ltime=L1time, ifname=True, towernum='1')
drawpic.drawpic(X, Y, Z, point=point2, Ltime=L2time, ifname=True, towernum='2')
drawpic.drawpic(X, Y, Z, point=point3, Ltime=L3time, ifname=True, towernum='3')
drawpic.drawpic(X, Y, Z, point=point4, Ltime=L4time, ifname=True, towernum='4')
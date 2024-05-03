import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = [None, 0, 52.44686, 45.83018, 0.97304, 27.53703, 21.9907, -18.887]
Y = [None, 0, 28.03828, 64.6438, 69.09432, 45.95162, 79.77557, -9.23483]
Z = [None, 0.824, 0.727, 0.742, 0.85, 0.786, 0.678, 0.575]
L = [None, 34.26078, 38.1548, 63.9268, 88.0549, 40.27062, 90.73614, 55.42816]
color = ['b', 'g', 'r', 'w', 'c', 'm', 'y']
centerlist = [(X[i+1], Y[i+1], Z[i+1]) for i in range(7)]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



for i in range(7):
    # 定义球心坐标和半径
    center = centerlist[i]
    radius = L[i+1]
    print(center, radius)
    ax.scatter(center[0], center[1], center[2], color=color[i], s=100, zorder=100000, alpha=0.3)
    # 生成球面上的数据点
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, np.pi, 50)
    theta, phi = np.meshgrid(theta, phi)

    x = center[0] + radius * np.sin(phi) * np.cos(theta)
    y = center[1] + radius * np.sin(phi) * np.sin(theta)
    z = center[2] + radius * np.cos(phi)

    # 绘制图形

    ax.plot_wireframe(x, y, z, color=color[i], alpha=0.1, zorder=2)

# 设置坐标轴范围
# ax.set_xlim(center[0] - radius, center[0] + radius)
# ax.set_ylim(center[1] - radius, center[1] + radius)
# ax.set_zlim(center[2] - radius, center[2] + radius)
# ax.plot(37.95, -5.81, 0.96)
# point = (37.95, -5.81, 0.96)
# ax.scatter(point[0], point[1], point[2], color='r', s=100, zorder=3)

point = (37.95, -5.81, 0.96)
ax.scatter(point[0], point[1], point[2], color='r', s=500, marker='*', zorder=100000)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

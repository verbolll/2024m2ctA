# drawpic.py
# 画出监测塔与音爆点三维图
import numpy as np
import matplotlib.pyplot as plt

def drawpic(X, Y, Z, point : tuple, ifname=False, Ltime=np.array([]), towernum=None, L=None):
    if Ltime != np.array([]):
        L = (Ltime*0.34 - 4.07997).tolist()
        L.insert(0, None)
        print(L)

    color = ['b', 'g', 'r', '#39CC4B', 'c', 'm', 'y']
    centerlist = [(X[i+1], Y[i+1], Z[i+1]) for i in range(7)]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(7):
        center = centerlist[i]
        radius = L[i+1]
        print(center, radius)
        ax.scatter(center[0], center[1], center[2], color=color[i], s=100, zorder=100000, alpha=0.3)
        if ifname:
            ax.scatter(center[0], center[1], center[2], color=color[i], s=100, zorder=100000, alpha=0.3, label='tower' + str(i+1))
        theta = np.linspace(0, 2*np.pi, 100)
        phi = np.linspace(0, np.pi, 50)
        theta, phi = np.meshgrid(theta, phi)
        x = center[0] + radius * np.sin(phi) * np.cos(theta)
        y = center[1] + radius * np.sin(phi) * np.sin(theta)
        z = center[2] + radius * np.cos(phi)
        ax.plot_wireframe(x, y, z, color=color[i], alpha=0.1, zorder=2)

    ax.scatter(point[0], point[1], point[2], color='black', s=500, marker='*', zorder=100000)
    if ifname:
        ax.scatter(point[0], point[1], point[2], color='black', s=100, marker='*', zorder=100000, label= 'boom' + str(towernum))
        plt.legend(loc='upper left')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

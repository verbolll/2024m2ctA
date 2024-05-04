import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 点的信息
points1 = {
'A': (0, 0, 0.824,                 'b'),
'B': (52.73877, 28.03828, 0.727,   'b'),
'C': (50.69538, 64.64380, 0.742,   'b'),
'D': (0.97304, 91.34692, 0.850,    'b'),
'E': (27.53703, 45.95162, 0.786,   'b'),
'F': (21.99070, 97.57765, 0.678,   'b'),
'G': (-18.87698, 35.27037, 0.575,  'b'),
}
points2 = {
'p1':(25.20188, 11.7937, 12.5139,    'r'),
'p2':(5.741, 49.6232, 11.4796,       'r'),
'p3':(44.662257, 49.62316, 13.46793, 'r'),
'p4':(25.201587, 83.0019,11.5288,    'r'),
}
points = points1.copy()
points.update(points2)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(121, projection='3d')
ax1 = fig.add_subplot(122)
x_values = []
y_values = []
z_values = []
colors = []
def draw2D(points, mk):
    x_values = [point[0] for point in points.values()]
    y_values = [point[1] for point in points.values()]
    z_values = [point[2] for point in points.values()]
    colors = [point[3] for point in points.values()]
    ax.scatter(x_values, y_values, z_values, c=colors, marker=mk,s=200, alpha=1)
    ax1.scatter(x_values, y_values, c=colors, marker=mk,s=200, alpha=1)

draw2D(points1, 'o')
draw2D(points2, '*')

for label, (x, y, z, _) in points.items():
    ax.text(x+0.6, y+0.6, z+0.6, label, fontsize=20)
ax.set_xlabel('X (km)')
ax.set_ylabel('Y (km)')
ax.set_zlabel('Z (km)')
ax.set_title('3D Scatter Plot')
for label, (x, y, _, _) in points.items():
    ax1.text(x+1, y, label, fontsize=20)
ax1.set_xlabel('X (km)')
ax1.set_ylabel('Y (km)')
ax1.set_title('Top View')
plt.tight_layout()
plt.show()
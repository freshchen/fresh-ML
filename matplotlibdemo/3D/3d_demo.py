import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d

"""
 @anthor LingChen
 @create 11/29/2018 3:56 PM
 @Description
"""

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
x = np.array([[1, 2, 3], [5, 6, 7]])
y = np.array([[5, 6, 7], [5, 2, 4]])
z = np.array([[1, 2, 6], [1, 2, 9]])
ax1.plot_wireframe(x, y, z)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()

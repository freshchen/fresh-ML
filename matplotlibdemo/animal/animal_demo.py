

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import style

"""
 @anthor LingChen
 @create 11/29/2018 10:50 AM
 @Description
"""
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animal1(i):
    data = np.loadtxt('../data/animal.txt', unpack=True)
    ax1.clear()
    ax1.plot(data[0], data[1])


ani = animation.FuncAnimation(fig, animal1, interval=1000)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

"""
 @anthor LingChen
 @create 11/29/2018 3:46 PM
 @Description
"""
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)
data = np.loadtxt('../data/test1.txt', unpack=True)
ax1.plot(data[0], data[1])
ax2.plot(data[0], data[1])
ax3.plot(data[0], data[1])
plt.xlabel('x')
plt.ylabel('y')
# plt.show()

plt.savefig('D:\\GIT\\fresh-blog\\source\\images\\sub1.png')

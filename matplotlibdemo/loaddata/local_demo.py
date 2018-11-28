import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 11/28/2018 4:02 PM
 @Description np.loadtxt不止可以读txt，其他csv文件也可以读
"""
data = np.loadtxt('../data/test1.txt', unpack=True)
plt.plot(data[0], data[1], label='Loaded from local file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

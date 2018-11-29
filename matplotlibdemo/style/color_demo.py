import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

"""
 @anthor LingChen
 @create 11/28/2018 4:50 PM
 @Description
"""
style.use('ggplot')
# 创建子图，1*1网格，起点（0，0）
fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))
ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')
# 数轴距离
ax1.set_yticks([0, 1.5, 2.5, 3.5])
data = np.array([[1, 2], [3, 4]])
# 填充
ax1.fill_between([0, 1], 0, [0, 1])
# 改边框
ax1.spines['left'].set_color('c')
ax1.spines['left'].set_linewidth(5)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.tick_params(axis='x', colors='#f06215')
plt.plot(data)
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.show()

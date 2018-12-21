import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 11/28/2018 2:30 PM
 @Description
"""
x = np.array([1, 2, 3])
y = np.array([5, 6, 7])
plt.plot(x, label='first line')
plt.plot(y, label='second line')
# 横坐标注释
plt.xlabel('Plot Number')
# 列坐标注释
plt.ylabel('Important var')
# 生成表标题
plt.title('Matplotlib demo\nCheck it out')
# 生成小方块显示每条线对应的label
plt.legend()
# plt.show()

plt.savefig('D:\\GIT\\fresh-blog\\source\\images\\twoline.png')

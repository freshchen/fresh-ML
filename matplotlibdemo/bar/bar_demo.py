import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 11/28/2018 2:53 PM
 @Description 条形图
"""
one = np.array([[1, 3, 5, 7, 9], [3, 4, 6, 12, 7]])
two = np.array([[2, 4, 6, 8, 10], [4, 2, 9, 8, 11]])
# 参数1是横坐标，参数2是高度
plt.bar(one[0], one[1], label='first')
plt.bar(two[0], two[1], label='second')
plt.xlabel('bar-hist Number')
# 列坐标注释
plt.ylabel('bar-hist height')
# 生成表标题
plt.title('Matplotlib demo\nCheck it out')
# 生成小方块显示每条线对应的label
plt.legend()
# plt.show()

plt.savefig('D:\\GIT\\fresh-blog\\source\\images\\bar1.png')

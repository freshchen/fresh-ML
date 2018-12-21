import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 11/28/2018 3:06 PM
 @Description 直方图
"""
# 原始数据
population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 102, 110, 120, 121, 122, 130, 111, 115, 112, 80, 75, 65,
                   54, 44, 43, 42, 48, 12, 32, 44, 9, 7]
# 横坐标，表示增量
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Matplotlib demo\nCheck it out')
# plt.show()

plt.savefig('D:\\GIT\\fresh-blog\\source\\images\\hist1.png')

import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 11/28/2018 3:56 PM
 @Description
"""
slices = [7, 2, 5, 11]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']
# slices是切片比例，startangle是起始角度，explode可以拿出不是0的切片
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')
plt.title('Matplotlib demo\nCheck it out')
# plt.show()

plt.savefig('D:\\GIT\\fresh-blog\\source\\images\\pie1.png')

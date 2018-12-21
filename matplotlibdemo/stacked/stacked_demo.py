import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 11/28/2018 3:44 PM
 @Description
"""

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], color='m', label='Sleeping', linewidth=2)
plt.plot([], [], color='c', label='Eating', linewidth=2)
plt.plot([], [], color='r', label='Working', linewidth=2)
plt.plot([], [], color='k', label='Playing', linewidth=2)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m',
                                                                'c', 'r', 'k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Matplotlib demo\nCheck it out')
plt.legend()
# plt.show()

plt.savefig('D:\\GIT\\fresh-blog\\source\\images\\stacked1.png')

import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 11/28/2018 3:22 PM
 @Description
"""
data = np.array([[1, 2], [2, 3], [5, 6]])
# marker有许多图标：https://matplotlib.org/api/markers_api.html
plt.scatter(data[:, 0], data[:, 1], label='skitscat', color='k', s=25, marker="o")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Matplotlib demo\nCheck it out')
plt.legend()
# plt.show()

plt.savefig('D:\\GIT\\fresh-blog\\source\\images\\scatter1.png')

import statisticallearning.KNN.knn as knn
import numpy as np

old_x = [3, 5]
k = 10
x = np.array([3, 5])
y = 'y'
print('训练数据：[%s,%s] k值：%s 结果：%s' % (old_x[0], old_x[1], k, knn._init_(x, k, y)))

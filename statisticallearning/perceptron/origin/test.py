import numpy as np
import statisticallearning.perceptron.origin.Perceptron as perception

weight, bias = perception._init_()
x = np.array([4, 0.5])
result = np.dot(weight, x) + bias
if result >= 0:
    print(1)
else:
    print(-1)

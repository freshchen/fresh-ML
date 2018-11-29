import random
import time

import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 11/29/2018 1:43 PM
 @Description
"""

for i in range(1, 50):
    with open('../data/animal.txt', 'a') as f:
        f.write('' + str(i) + '  ' + str(random.randint(1, 20)) + '\n')
        time.sleep(3)

import matplotlib.pyplot as plt
import numpy as np

"""
 @anthor LingChen
 @create 12/4/2018 4:21 PM
 @Description
"""


def quick_mod(a, p, n):
    result = a % n
    remainders = []
    while p != 1:
        remainders.append(p & 1)
        p = p >> 1
    print(remainders)
    while remainders:
        rem = remainders.pop()
        result = ((a ** rem) * result ** 2) % n
    return result


print(quick_mod(3, 9, 2))

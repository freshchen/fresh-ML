import matplotlib.pyplot as plt
import numpy as np
from enum import Enum, unique

"""
 @anthor LingChen
 @create 11/29/2018 5:11 PM
 @Description
"""


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = '周五'
    Sat = 6


if __name__ == '__main__':
    print(Weekday.Fri.value)

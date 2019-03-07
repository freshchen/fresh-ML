import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import svm

"""
 @anthor LingChen
 @create 12/27/2018 3:05 PM
 @Description
"""

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1:])

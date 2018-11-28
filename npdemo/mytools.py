import numpy as np


def check_array(ary):
    if type(ary) == "<class /'numpy.ndarray/'>":
        return "please input a ndarray"
    else:
        print("info is {size:%s ndim:%s shape:%s dtype:%s}" % (np.size(ary), np.ndim(ary), np.shape(ary), ary.dtype))

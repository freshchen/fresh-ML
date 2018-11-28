import sys

import numpy as np


# 创建n*n的方阵
def init_array(line_num, num):
    # data1 = []
    # data2 = []
    # temp1 = line_num
    # temp2 = line_num
    # while temp1 > 0:
    #     data2.append(num)
    #     temp1 = temp1 - 1
    # while temp2 > 0:
    #     data1.append(data2)
    #     temp2 = temp2 - 1
    data1 = []
    temp = line_num * line_num
    while temp > 0:
        data1.append(num)
        temp = temp - 1
    ary = np.array(data1).reshape(line_num, line_num)
    return ary


def cut_array(ary, num, cut_num):
    num1 = num - cut_num
    num2 = 2 * num - num1 - 1
    ary[num1:num2, num1:num2] = cut_num
    return ary


def main(param):
    num = param
    if num < 0:
        return "please input num > 0"
    else:
        line_num = 2 * num - 1
        ary = init_array(line_num, num)
        cut_num = num
        # 循环替换
        while cut_num > 0:
            cut_num = cut_num - 1
            cut_array(ary, num, cut_num)
        print(ary)
        return ary


# 数字n从java程序调用Scanner获得并传入python脚本
main(int(sys.argv[1]))

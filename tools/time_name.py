import time
import datetime


def init_file_name(name, for_mat):
    date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    dir = 'D:\\info\\screenshot\\'
    str_date = str(date)
    file_name = name + '-' + str_date
    result = dir + file_name + '.' + for_mat
    return result


def get_now_format():
    date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return date

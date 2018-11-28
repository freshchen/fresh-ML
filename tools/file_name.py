import time
import datetime


def init_file_name(name, for_mat):
    t = time.time()
    date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    dir = 'D:\\info\\screenshot\\'
    str_date = str(date)
    file_name = name + '-' + str_date
    result = dir + file_name + '.' + for_mat
    return result

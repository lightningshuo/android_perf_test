# coding= utf-8
# NAME: utils
# AUTHOR:SHUO
import time

def date_time():
    return time.strftime("%m%d-%H",time.localtime())

if __name__ == '__main__':
    print(date_time())
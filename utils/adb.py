# coding= utf-8
# NAME: adb.py
# AUTHOR:SHUO
import subprocess
def get_package():
    """
    获取当前的package
    :return:
    """
    #方法一
    cmd_info  = subprocess.getoutput("adb shell dumpsys window windows|findstr mFocusedApp")
    return cmd_info.split("u0 ")[-1].split("/")[0]

    #方法二

def get_current_activity():
    """
    获取当前的activity
    :return:
    """
    pass

def get_memory():
    pass

def get_cpuinfo():
    pass

if __name__ == '__main__':
    print(type(get_package()))
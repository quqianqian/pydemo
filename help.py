import sys
import time


def demo():
    a = input("请输入要查询的命令：")
    moment = time.localtime()
    print("time = %s" % time)
    # print("你输入的是%s" % a)
    if a:
        help(a)
    else:
        print(dir(sys.modules['builtins']))


if __name__ == '__main__':
    demo()
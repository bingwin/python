# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 回调，其实就是把一个函数作为参数传递给另一个函数；回调可以是同步的也可以是异步的；同步异步和单线程多线程没有关系。
# 或者说，同步也可以是单线程也可以是多线程；异步则必须是多线程或者多进程（每个进程可以是单线程）。
# 同步回调就是：把函数b传递给函数a。执行a的时候，回调了b，a要一直等到b执行完才能继续执行；
# 异步回调就是：把函数b传递给函数a。执行a的时候，回调了b，然后a就继续往后执行，b独自执行。－－－请注意这里不要和多线程纠缠起来：线程是存在于一个进程里的，而异步回调可能是好几个进程。
# （协程）


# 这个被传入的、后又被调用的函数就称为回调函数（callback function）
import time

def callback():
    print("这是一个callback函数")

def tes_callback(call):
    print("这是在test_callback中哦")
    #模拟延时效果
    time.sleep(1)
    print("开始调用callback函数")
    time.sleep(1)
    #开始回调
    call()
    print("调用完成")

if __name__ == '__main__':
    tes_callback(callback)
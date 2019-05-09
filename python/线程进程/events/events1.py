# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# Event是线程间通信最间的机制之一：一个线程发送一个event信号，其他的线程则等待这个信号。用于主线程控制其他线程的执行。
# Events 管理一个flag，这个flag可以使用set()设置成True或者使用clear()重置为False，wait()则用于阻塞，在flag为True之前。flag默认为False。
#
# Event.wait([timeout]) ： 堵塞线程，直到Event对象内部标识位被设为True或超时（如果提供了参数timeout）
# Event.set() ：将标识位设为Ture
# Event.clear() ： 将标识伴设为False
# Event.isSet() ：判断标识位是否为Ture

import threading

def do(event):
    print('start')
    event.wait()
    print('execute')


event_obj = threading.Event()
for i in range(5):
    t = threading.Thread(target=do, args=(event_obj,))
    # t = threading.Thread(target=do, args=(event_obj)
    t.start()

event_obj.clear()
inp = input('input:')
if inp == 'true':
    event_obj.set()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (threadName, time.ctime(time.time()))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print "Error: unable to start thread"

while 1:
    pass

# 并发性: 并发处理的是处理来自不同线程的共享状态访问 并发系统时的一个重要问题是在多个线程或进程间共享数据。
# 并行性: 并行可定义为将任务分解为可同时处理的子任务的技术。 如上所述，它与并发性相反，其中两个或更多事件同时发生


# 僵局 - 餐饮哲学家的问题



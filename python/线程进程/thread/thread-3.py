#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    while not exitFlag:                             # 启动程序后 线程一直在运行  函数也一直在运行  至到wordqueue赋值
        print("测试。。。")                           # 线程一直在运行 函数也一直在运行 每次次数显示不同
        queueLock.acquire()                         # 获得锁的次数和print("测试。。。") 次数相同 而不是5次
        if not workQueue.empty():
            data = q.get()                          # 每次获得一个数据
            queueLock.release()
            print "%s processing %s" % (threadName, data)
            print("test")                           # 每次获得一个数据 只有5个数据 所以只能输出5次
        else:
            queueLock.release()
        print("测试2。。。。")                        # 线程一直在运行 函数也一直在运行 每次次数显示不同
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"


# Queue.Queue(maxsize=0)
# FIFO即First in First Out,先进先出。Queue提供了一个基本的FIFO容器，使用方法很简单,maxsize是个整数，指明了队列中能存放的数据个数的上限。
# 一旦达到上限，插入会导致阻塞，直到队列中的数据被消费掉。如果maxsize小于或者等于0，队列大小没有限制

# Queue.put(item) 写入队列，timeout等待时间


# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 当等待一项服务时，对日常生活中的排队很熟悉。 队列数据结构同样意味着数据元素排列在一个队列中。 队列的唯一性在于项目添加和删除的方式。
# 这些对象可以放在最后，但从另一端移除。 所以这是先进先出的方法。 可以使用python list实现队列，可以使用insert()和pop()方法添加和移除元素。它们没有插入，因为数据元素总是添加在队列的末尾。

class Queue(object):

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False
# Pop method to remove element
  def removefromq(self):
      if len(self.queue) > 0:
          return self.queue.pop()
      return ("No elements in Queue!")

TheQueue = Queue()
print("队列")
TheQueue.addtoq("Mon")
print(TheQueue.queue[0])
TheQueue.addtoq("Tue")
print(TheQueue.queue[0])
TheQueue.addtoq("Wed")
print(TheQueue.queue[0])
print(TheQueue.removefromq())
print(TheQueue.removefromq())
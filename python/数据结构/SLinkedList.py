# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 在有些情况下，存储数据的内存分配不能位于连续的内存块中。 所以接受指针的帮助，其中数据和数据元素的下一个位置的地址也被存储。
# 所以从当前数据元素的值中知道下一个数据元素的地址。通常这样的结构被称为指针。 但在Python中，将它们称为节点。节点是各种其他数据结构链表和树在python中处理的基础
class daynames:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')

e1.nextval = e3                     # 对象的一个属性是下一个对象
e3.nextval = e2
e2.nextval = e4
print("节点")
thisvalue = e1

while thisvalue:
        print(thisvalue.dataval)
        thisvalue = thisvalue.nextval

print("——————————————————————————————————————————")

# 链表是一系列数据元素，通过链接连接在一起。 每个数据元素都以指针的形式包含到另一个数据元素的连接。
# 遍历链表
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
print("链表")

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list1.listprint()


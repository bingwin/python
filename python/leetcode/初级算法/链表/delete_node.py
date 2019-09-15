# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
#
# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:

# 输入: head = [4, 5, 1, 9], node = 5
# 输出: [4, 1, 9]
# 解释: 给定你链表中值为
# 5
# 的第二个节点，那么在调用了你的函数之后，该链表应变为
# 4 -> 1 -> 9.
# 示例
# 2:
#
# 输入: head = [4, 5, 1, 9], node = 1
# 输出: [4, 5, 9]
# 解释: 给定你链表中值为
# 1
# 的第三个节点，那么在调用了你的函数之后，该链表应变为
# 4 -> 5 -> 9.
#
# 说明:
#
# 链表至少包含两个节点。
# 链表中所有节点的值都是唯一的。
# 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
# 不要从你的函数中返回任何结果。


class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

e4 = Node('4')
e5 = Node('5')
e1 = Node('1')
e9 = Node('9')

e4.nextval = e5                     # 对象的一个属性是下一个对象
e5.nextval = e1
e1.nextval = e9
#
# print(e4.nextval.dataval)       # 5
# print(e5.nextval.dataval)       # 1
# print(e1.nextval.dataval)       # 9
# print(e9.nextval.dataval)


# 官方
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.dataval, node.nextval = node.nextval.dataval, node.nextval.nextval

if __name__ == "__main__":
    deleteNode(e5)
    print(e4.nextval.dataval)
    print(e5.nextval.dataval)
    print(e1.nextval.dataval)

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

import string


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


e4 = Node('4')
e5 = Node('5')
e1 = Node('1')
e9 = Node('9')

e4.next = e5  # 对象的一个属性是下一个对象
e5.next = e1
e1.next = e9

d4 = Node('4')
d5 = Node('5')
d1 = Node('1')

d4.next = d5  # 对象的一个属性是下一个对象
d5.next = d1

# 需要进行倒序
def add_two_numbers(l1, l2):
    a1 = []
    a2 = []
    c = []
    while l1 is not None:
        a1.append(l1.val)
        l1 = l1.next
    while l2 is not None:
        a2.append(l2.val)
        l2 = l2.next
    s1 = "".join(a1)
    s2 = "".join(a2)
    i1 = int(s1) + int(s2)
    s3 = str(i1)
    for i in range(0, len(s3)):
        l = Node(s3[i])
        c.append(l)
    for i in range(0, len(c)):
        if i < len(c) - 1:
            c[i].next = c[i + 1]
    return c[0]


if __name__ == "__main__":
    print(add_two_numbers(e4, d4).next.val)

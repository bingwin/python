# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


e1 = Node(1)
e2 = Node(2)
e4 = Node(4)

e1.nextval = e2  # 对象的一个属性是下一个对象
e2.nextval = e4

d1 = Node(1)
d3 = Node(3)
d4 = Node(4)
# d5 = Node(5)


d1.nextval = d3  # 对象的一个属性是下一个对象
d3.nextval = d4
# d4.nextval = d5


# 自己
# 思路不是很对 没有比较一个链表完了之后的情况
# def mergetwolists(l1, l2):
#     l3 = None
#     while (l1.dataval is not None) and (l2.dataval is not None):
#         print(1)
#         if l1.dataval < l2.dataval:
#             Temp = Node(l1.dataval)
#             if l3 is not None:
#                 l3.nextval = Temp
#                 l3 = Temp
#             else:
#                 l3 = Temp
#             l1.dataval = l1.nextval.dataval         # 没有赋值过去
#         if l1.dataval > l2.dataval:
#             Temp = Node(l2.dataval)
#             if l3 is not None:
#                 l3.nextval = Temp
#                 l3 = Temp
#             else:
#                 l3 = Temp
#             l2.dataval = l2.nextval.dataval
#
#         if l1.dataval == l2.dataval:
#             Temp1 = Node(l1.dataval)
#             Temp2 = Node(l2.dataval)
#             if l3 is not None:
#                 l3.nextval = Temp1
#                 Temp1.nextval = Temp2
#                 l3 = Temp2
#             else:
#                 l3 = Temp2
#                 Temp2.nextval = Temp1
#                 l3 = Temp1
#
#             l1.dataval = l1.nextval.dataval
#             l2.dataval = l2.nextval.dataval
#
#     return l3

# 自己
# 感觉链表还是借助数组帮助比较合适 实际中不一定允许


# 答案
# 我们直接将以上递归过程建模，首先考虑边界情况。
# 特殊的，如果 l1 或者 l2 一开始就是 null ，那么没有任何操作需要合并，所以我们只需要返回非空链表。
# 否则，我们要判断 l1 和 l2 哪一个的头元素更小，然后递归地决定下一个添加到结果里的值。如果两个链表都是空的，那么过程终止，所以递归过程最终一定会终止。

def mergetwolists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.dataval < l2.dataval:
        l1.nextval = mergetwolists(l1.nextval, l2)              # 小的元素的下一个元素 是函数运行后的下一个小元素
        return l1
    else:
        l2.nextval = mergetwolists(l1, l2.nextval)
        return l2



if __name__ == "__main__":
    print(mergetwolists(d1, e1).nextval.dataval)
    # print()
    print(d1.nextval.dataval)
    print(e1.nextval.dataval)
    print(e2.nextval.dataval)
    # print(d4.nextval.dataval)
    print(e4.nextval.dataval)


#   e1.ne = me(d1,e2)   e1.ne = d1
#    re e1
#   d1.ne = me(d3,e2)
#    re d1
#   e2.ne = me(d3,e4)
#    re e2
#   d3.ne = me(d4,e4)
#    re d3
#   e3.ne = me(d4,None)
#    re e4
#

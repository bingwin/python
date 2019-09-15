# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


e4 = Node('4')
e5 = Node('5')
e1 = Node('1')
e9 = Node('9')

e4.nextval = e5  # 对象的一个属性是下一个对象
e5.nextval = e1
e1.nextval = e9

# 自己 借助list
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    p = head
    l = []
    while p is not None:
        l.append(p)
        p = p.nextval
    de = l[-n]
    de.dataval, de.nextval = de.nextval.dataval, de.nextval.nextval
    return l


# 答案
# 快慢指针
# 方法二：一次遍历算法
#
# 算法
#
# 上述算法可以优化为只使用一次遍历。我们可以使用两个指针而不是一个指针。第一个指针从列表的开头向前移动
# n+1 步，而第二个指针将从列表的开头出发。现在，这两个指针被
# n 个结点分开。我们通过同时移动两个指针向前来保持这个恒定的间隔，直到第一个指针到达最后一个结点。
# 此时第二个指针将指向从最后一个结点数起的第
# n 个结点。我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点

# 快慢指针 （参考官方题解二）
#
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         front=ListNode(0)
#         front.next,fast,slow=head,front,front
#         while(n or fast):
#             if n:fast,n=fast.next,n-1
#             else:
#                 fast=fast.next
#                 slow=slow.next if fast else slow
#         slow.next=slow.next.next
#         return front.next


if __name__ == "__main__":
    print(removeNthFromEnd(e4, 2))
    print(e4.nextval.dataval)
    print(e5.nextval.dataval)
    # print(e1.nextval.dataval)


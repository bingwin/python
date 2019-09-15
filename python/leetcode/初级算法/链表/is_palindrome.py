# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# 答案 借助list
# class Solution(object):
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         res = []
#         while(head):
#             res.append(head.val)
#             head = head.next
#
#         if len(res) <= 1: # ps: 空链表和单个结点的链表都是回文链表
#             return True
#         else:
#             n = len(res)
#             for i in range(n//2):
#                 if res[i] != res[n-1-i]:
#                     return False
#             return True

# 答案 没有list
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


def isPalindrome(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    curr = slow
    while curr:
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp
    while head and prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next

    return True


if __name__ == "__main__":
    print(isPalindrome(e1))

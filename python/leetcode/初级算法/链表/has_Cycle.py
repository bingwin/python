# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个链表，判断链表中是否有环。
# #
# # 为了表示给定链表中的环，我们使用整数
# # pos
# # 来表示链表尾连接到链表中的位置（索引从
# # 0
# # 开始）。 如果
# # pos
# # 是 - 1，则在该链表中没有环。
# #
# #
# #
# # 示例
# # 1：
# #
# # 输入：head = [3, 2, 0, -4], pos = 1
# # 输出：true
# # 解释：链表中有一个环，其尾部连接到第二个节点。
# #
# #
# # 示例
# # 2：
# #
# # 输入：head = [1, 2], pos = 0
# # 输出：true
# # 解释：链表中有一个环，其尾部连接到第一个节点。
# #
# #
# # 示例
# # 3：
# #
# # 输入：head = [1], pos = -1
# # 输出：false
# # 解释：链表中没有环。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 答案 奇葩的解法
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == 'bjfuvth':           # 如果发现元素为bjfuvth，那么就是循环了
                return True
            else:
                head.val = 'bjfuvth'            # 把每一个赋值为bjfuvth
            head = head.next
        return False

# 答案 置空法
# def hasCycle(self, head):
#     if not head:
#         return False
#     while head.next and head.val != None:
#         head.val = None  # 遍历的过程中将值置空
#         head = head.next
#     if not head.next:  # 如果碰到空发现已经结束，则无环
#         return False
#     return True  # 否则有环

# 答案 可以使用快慢置针 如果相遇 则有环 如果不相遇 则没有环


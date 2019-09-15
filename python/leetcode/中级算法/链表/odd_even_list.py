# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:
#
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

e4 = Node('4')
e5 = Node('5')
e1 = Node('1')
e9 = Node('9')
e3 = Node('3')

e4.next = e5  # 对象的一个属性是下一个对象
e5.next = e1
e1.next = e9
e9.next = e3

# 自己
# def odd_even_list(l1):
#     h1 = l1
#     while h1.next.next is not None:         # 最后一个h1没有next属性 会报错
#         print(h1.next.val)
#         h1.next = h1.next.next
#         h1 = h1.next
#     h1.next = l1.next
#     while h1.next.next is not None:
#         h1.next = h1.next.next
#         h1 = h1.next
#     return h1.next.val


# 答案
def odd_even_list(head):
   if head == None: return head
   point1, point2 = head, head.next
   p1, p2 = point1, point2
   while p2 != None and p2.next:
       p1.next = p1.next.next
       p2.next = p2.next.next
       p1 = p1.next
       p2 = p2.next
   p1.next = point2
   return point1.next.val

if __name__ == "__main__":
    print(odd_even_list(e4))

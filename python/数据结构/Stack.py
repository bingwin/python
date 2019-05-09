# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 在堆栈中，顺序排列的最后一个元素将首先出现，因为只能从堆栈顶部移除。 这种功能称为后进先出(LIFO)功能。 添加和删除元素的操作称为PUSH和POP。
# 在下面的程序中，我们将它实现为add和remove函数。首先声明一个空列表并使用append()和pop()方法来添加和删除数据元素。
# 这里的"堆栈"指的就是栈，先进后出

class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
print("堆栈")

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
print(AStack.remove())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
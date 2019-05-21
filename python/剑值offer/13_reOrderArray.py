# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。


# 自己
def reOrderArray(n):
    list1 = []
    list2 = []
    for i in n:
        if i % 2 == 1:
            list1.append(i)
        if i % 2 == 0:
            list2.append(i)
    return list1 + list2

s = reOrderArray([3, 3, 4, 5, 6, 1])
print(s)

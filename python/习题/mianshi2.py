# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# Python面试真题】- 介绍一下Python下range()函数的用法
i = range(10)
print(i)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

i = range(1, 10)
print(i)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = range(0, 9, 2)
print(i)
# [0, 2, 4, 6, 8]

i = range(99, 0, -10)
print(i)
# [99, 89, 79, 69, 59, 49, 39, 29, 19, 9]

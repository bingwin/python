# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

# 匿名函数
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)

L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
print sorted(L, key=lambda x: x[1])
# print(sorted(L,key=x[1]))


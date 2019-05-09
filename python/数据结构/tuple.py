# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
# tuple的元素不能该变，它也没有append()，insert()这样的方法。
# 元祖 不可变的列表称为元祖      相当于数组

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7, 8)

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
print ("tup2[1:]: ", tup2[1:])

# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


# 元组内置函数
# 序号	方法及描述
# 1	cmp(tuple1, tuple2)
# 比较两个元组元素。
# 2	len(tuple)
# 计算元组元素个数。
# 3	max(tuple)
# 返回元组中元素最大值。
# 4	min(tuple)
# 返回元组中元素最小值。
# 5	tuple(seq)
# 将列表转换为元组。

print("——————————————————————————————————————————————————")


from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print(p.x, p[1])


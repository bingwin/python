# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 判断一个变量是否是某个类型可以用isinstance()判断：

from collections import Iterable

s1 = isinstance('abc', Iterable)  # str是否可迭代  # True

s2 = isinstance([1, 2, 3], Iterable)  # list是否可迭代  # True

s3 = isinstance(123, Iterable)  # 整数是否可迭代 False

a = [1, 2, 3]

s4 = isinstance(a, list)  # 整数是否可迭代 False

print(s1, s2, s3, s4)


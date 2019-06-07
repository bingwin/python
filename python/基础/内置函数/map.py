#!/usr/bin/python
# -*- coding: UTF-8 -*-


def square(x):  # 计算平方数
    return x ** 2


s = map(square, [1, 2, 3, 4, 5])
print(s)


z = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(z)
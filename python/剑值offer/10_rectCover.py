# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import math

def rectCover(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return rectCover(n-1) + rectCover(n-2)

def rectCover_2(number):
    # write code here
    if number == 0:
        return 0
    if number == 1:
        return 1
    a, b = 1, 1
    while number > 1:
        a, b = b, a + b
        number -= 1
    return b



print(rectCover(10),rectCover_2(10))
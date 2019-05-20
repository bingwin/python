# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import math

def rectCover(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        i = n / 2
        s = pow(2, i)
    return s

print(rectCover(11))
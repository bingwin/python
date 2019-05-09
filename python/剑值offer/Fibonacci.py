# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39

# 自己
def fab(max):
    if max <= 39:
        n, a, b = 0, 0, 1
        while n < max:
            # a = b
            # b = a + b
            a, b = b, a + b     # 同时赋值
            n = n + 1
        return a
    if max > 39:
        return 0

print(fab(1))

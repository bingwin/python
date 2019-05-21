# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法

# 依旧是斐波那契数列
# 2*n的大矩形，和n个2*1的小矩形
# 其中target*2为大矩阵的大小

# 第一次摆放一块 2*1 的小矩阵，则摆放方法总共为f(target - 1)
# 第一次摆放一块1*2的小矩阵，则摆放方法总共为f(target-2)
# 要考虑顺序 不是2的n次方

# 自己
def rectCover(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return rectCover(n-1) + rectCover(n-2)

# 答案
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
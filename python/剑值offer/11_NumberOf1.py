# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。


# 自己
def numberof1(n):
    if n > 0:
        s = bin(n)
        count = 0
        for i in s:
            print(i)
            if i == "1":
                count = count + 1
        return count

    if n == 0 :
        return 0

    # if n < 0 :

# 答案
def NumberOf1(n):
    # write code here
    return sum([(n >> i & 1) for i in range(0, 32)])

print(numberof1(-10), NumberOf1(-10))


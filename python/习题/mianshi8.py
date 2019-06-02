# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 判断输入的正整数是不是回文数
# 回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

def hiuiwen(a):
    s = list(a)
    for i in range(len(s)/2):
        if s[i] == s[len(s)-i-1]:
            return 1
        else:
            return 0


# a = '312312552'
# s = list(a)
# print(s[-1])
# print(s[-2])
# print(s[len(s)-1])
# print(7/2)

print(hiuiwen("123212"))

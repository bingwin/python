# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# 自己
# def replaceSpace(a):
#     b = a.split()
#     s = ""
#     for i in range(b.__len__()):
#         b[i] = str(b[i])
#         s = s + b[i] + "%20"
#     s = s[0:-3]
#     return s

# 答案
def replaceSpace(s):
    # write code here
    s = list(s)
    count=len(s)
    for i in range(0,count):
        if s[i]==' ':
            s[i]='%20'
    return ''.join(s)

a = "We Are Happy"
print(replaceSpace(a))


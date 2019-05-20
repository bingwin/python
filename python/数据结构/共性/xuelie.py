# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 任何序列(或可以迭代的对象)都可以通过一个简单的赋值操作来分解为单独的变量.
# 字符串，文件，迭代器以及生成器。
p = (4, 5)
x, y = p
print(x)

# data = ['ACME', 50, 91.1, 312]
# name, share, price = data
# print(name)


name, share, price = ['ACME', "50", "91.1"]
print(name)

s = 'hello'
a, b, c, d, e = s
print(c)

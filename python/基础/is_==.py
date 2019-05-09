# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

x = [1, 2, 3]
y = [1, 2, 3]
print(id(x))
print(x == y)  # 比较的是数值    相同
print(x is y)  # 比较的是内存地址  不同
x.append(4)
print(x == y)   # 新加值后 不同
print(id(x))

t1 = 'ABC'
t2 = 'ABC'
print(id(t1), id(t2))   # 字符串相同，因为因为都指向的是'ABC'字符串的内存地址

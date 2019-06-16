# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# Counter是一个简单的计数器，例如，统计字符出现的个数：

from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
# print(c[ch])
print(c)

a = [1, 23, 4, 23, 4, 12]
for ch in a:
    c[ch] = c[ch] + 1
# print(c[ch])
print(c)

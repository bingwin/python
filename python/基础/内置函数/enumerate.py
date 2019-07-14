# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print i, element

# 0 one
# 1 two
# 2 three
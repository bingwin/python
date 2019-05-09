# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

def gen_AB():
    print("start")
    yield 'A'
    print('continue')
    yield 'B'
    print('end')


for c in gen_AB():
    print('---', c)

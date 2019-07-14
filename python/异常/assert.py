# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

i = 1
print(1)
print(2)
print(3)
print(i)                # 按向下箭头进行调试
print(4)
print(5)
a = 1
b = 2


assert 1 == 1   # 正常
# assert 1 == 0   # 如果编写时是错误的 后面的一行会提示错误

assert a == b   # 如果无法办法 后面的一行不会提示错误    运行时才提示错误

# assert 1 == 0   #相当于if,false会报错   程序停止
print(6)
# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

#如果try里面的句子成功执行，那么执行else的语句
try:
    1/1
    # print(1)
except:
    print(2)
else:
    print(3)
# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import import_def_test

A = import_def_test.add(1, 2)
print(A)


from import_class_test import C
# import import_class_test

B = C()
c = B.add_1(1, 2)
print(B)
print(c)


import sys
sys.path.append('..')  # 将当前模块上级目录路径加到当前模块扫描的路径里
from importtest1.import_test_2 import D
d = D()
e = d.add_2(4, 2)
print(e)

# __init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件。


from bao import import_class_test

c = import_class_test.C()
c.add_1(1,  2)




# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 1. Python字典浅复制
#
# 直接使用“=”是浅复制，比如有一个字典a，然后令b=a，这样的话当你改变b之后，a的内容也会一并改变。
#

import copy

a = {"name": "Leo", "age": 19}
b = a
print(id(a), id(b))
a["312"] = 312  # dict没有添加的方法 直接赋值就可以
print(a, b)

# 2. 深复制
#
# Python有一个copy库可以用于深复制。
# 这样，更改b的内容就不会影响a，更改a的内容也不会影响b。
c = copy.deepcopy(a)
a["3124"] = 13231
print(id(a), id(c))
print(a, c)

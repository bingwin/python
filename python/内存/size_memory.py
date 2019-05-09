# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


import sys
a = 100
b = True
c = 100L
d = 1.1
e = ""
f = []
g = ()
h = {}
i = set([])

print " %s size is %d "%(type(a),sys.getsizeof(a))
print " %s size is %d "%(type(b),sys.getsizeof(b))
print " %s size is %d "%(type(c),sys.getsizeof(c))
print " %s size is %d "%(type(d),sys.getsizeof(d))
print " %s size is %d "%(type(e),sys.getsizeof(e))
print " %s size is %d "%(type(f),sys.getsizeof(f))
print " %s size is %d "%(type(g),sys.getsizeof(g))
print " %s size is %d "%(type(h),sys.getsizeof(h))
print " %s size is %d "%(type(i),sys.getsizeof(i))


#  <type 'int'> size is 12
#  <type 'bool'> size is 12
#  <type 'long'> size is 14
#  <type 'float'> size is 16
#  <type 'str'> size is 21
#  <type 'list'> size is 36
#  <type 'tuple'> size is 28
#  <type 'dict'> size is 140
#  <type 'set'> size is 116
# 64位python一个int要24字节呢，如果定义了Py_TRACE_REFS，一个int要40字节呢。多出来的都是用于解释器的字节，
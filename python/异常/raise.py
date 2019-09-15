# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

try:
     s = None
     if s is None:
         print "s 是空对象"
         raise NameError     #如果引发NameError异常，后面的代码将不能执行
     print len(s)  #这句不会执行，但是后面的except还是会走到
except TypeError:
     print "空对象没有长度"
except NameError:
     print "1空对象没有长度"



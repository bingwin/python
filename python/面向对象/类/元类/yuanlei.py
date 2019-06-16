# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

class ObjectCreator(object):
    pass


print ObjectCreator

# 函数type实际上是一个元类。type就是Python在背后用来创建所有类的元类


# 你可以在写一个类的时候为其添加__metaclass__属性,定义了__metaclass__就定义了这个类的元类。

# class Foo(object):   #py2
#     __metaclass__ = something…
#
#
# class Foo(metaclass=something):   #py3
#     __metaclass__ = something…



def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    #通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)#返回一个类

class Foo(object):
    __metaclass__ = upper_attr
    bar = 'bip'

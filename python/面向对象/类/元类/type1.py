# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# bytes是Python 3中特有的，Python 2 里不区分bytes和str。

# bytes是byte的序列，而str是unicode的序列。

# 实际应用中在互联网上是通过二进制进行传输，所以就需要将str转换成bytes进行传输，
# 而在接收中通过decode()解码成我们需要的编码进行处理数据这样不管对方是什么编码而本地是我们使用的编码这样就不会乱码。


print(type(b'xxxx'))
print(type('xxxx'))

i = 10
print(type(i))
print(type(int))
print(type(int(312412)))


# bytearray和bytes不一样的地方在于，bytearray是可变的。




# 元类是python比较高级的用法，简而言之，元类就是创建类的类。
#
# 而type就是一个元类，是用来创建类对象的类。
#
# 因此，要定义元类就要使其继承type类。
#
# 通常情况下，开发者在使用OOP的方式编程时，往往会用到__init__方法，即构造函数。
#
# 该方法会在类初始化时运行。但是我们可以将验证的时机提前，以至于提前到类创建之时，因此就会用到__new__方法。

print("——————————————————————————————————————————————————")

# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass   # 指示使用ListMetaclass来定制类

# 当我们写下__metaclass__ = ListMetaclass语句时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
#
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
#
# __new__()方法接收到的参数依次是：
#
# 当前准备创建的类的对象；
#
# 类的名字；
#
# 类继承的父类集合；
#
# 类的方法集合。


# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 通常情况下，在类中定义的所有函数（注意了，这里说的就是所有，跟self啥的没关系，self也只是一个再普通不过的参数而已）都是对象的绑定方法，对象在调用绑定方法时会自动将自己作为参数传递给方法的第一个参数。
# 除此之外还有两种常见的方法：静态方法和类方法，二者是为类量身定制的，但是实例非要使用，也不会报错。

import time

class Foo(object):
    @staticmethod  # 装饰器  # 类中的一个函数，千万不要懵逼，self和x啥的没有不同都是参数名
    def spam(x, y, z):
        print(x, y, z)

print(type(Foo.spam)) # 类型本质就是函数
Foo.spam(1, 2, 3)  # 调用函数应该有几个参数就传几个参数

f1 = Foo()
f1.spam(3, 3, 3)  # 实例也可以使用,但通常静态方法都是给类用的,实例在使用时丧失了自动传值的机制


# 编写类时需要采用很多不同的方式来创建实例，而我们只有一个__init__函数，此时静态方法就派上用场了

# 尽管classmethod和staticmethod非常的相似，但是两者在具体的使用上还是有着细微的差别：classmethod必须使用类对象作为第一个参数，而staticmethod则可以不传递任何参数。
# 那么staticmethod又是什么呢？它和classmethod非常的相似，但是不强制要求传递参数（但是做的事与类方法或实例方法一样

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @staticmethod
    def now():  # 用Date.now()的形式去产生实例,该实例用的是当前时间
        t = time.localtime()  # 获取结构化的时间格式
        return Date(t.tm_year, t.tm_mon, t.tm_mday)  # 新建实例并且返回
    @staticmethod
    def tomorrow():  # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t = time.localtime(time.time()+86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

a = Date(1987, 11, 27)  # 自己定义时间
b = Date.now()  # 采用当前时间
c = Date.tomorrow()  # 采用明天的时间

print(a.year, a.month, a.day)
print(b.year, b.month, b.day)
print(c.year, c.month, c.day)


class Date1:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def now(cls, time1):  # 用Date.now()的形式去产生实例,该实例用的是当前时间          # 备选构造方法
        t = time.localtime()  # 获取结构化的时间格式
        print(time1)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)  # 新建实例并且返回

    @classmethod
    def tomorrow(cls, time2):  # 用Date.tomorrow()的形式去产生实例,该实例用的是明天的时间
        t = time.localtime(time.time()+86400)
        print(time2)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    def test1(self, name):         # python没有重载的概念  以定义的第一个函数为主
        print(name)

    def test1(self):
        print(1)



a = Date1(1987, 11, 27)  # 自己定义时间
b = Date1.now(412)  # 采用当前时间
c = Date1.tomorrow(3123)  # 采用明天的时间
a.test1()

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 默认情况下每个类都会有一个dict，这个dict维护了实例的所有属性，每个实例都有一个dict，并且通过__dict__访问。通过如下的例子来说明这个dict的使用。

class Test(object):
    x = 9  # 类变量

    def __init__(self, z):
        self.z = z

t1 = Test(2)
t2 = Test(3)
t1.y = 8  # 给实例绑定一个属性
t2.x = 5  # 即使不在初始化函数内 也可以调用
print(t1.__dict__)
print(t2.__dict__)



# 然而在某些情况下，我们运行前就知道了某个类需要的属性时，这个dict就有点浪费内存，特别是当需要创建大量的实例时，内存浪费更加明显。而在新式类中，我们可以借助__slots__解决这个问题。
#
# __slots__中我们限制了能够添加的属性，并为每个空间恰好预留足够的空间来保存变量，如此一来，python也不再使用dict。


class Test1(object):
    __slots__ = ('x')

    def __init__(self):
        pass


t = Test1()
t.x = 9
print(t.x)
# t.y=0   #显示没有y这个属性，除了__slots__内的其他都不能绑定
# print(t.y)
# print(t.__dict__)  # 显示已无__dict__属性
print(t.__slots__)
# t.y = 10           # y在slots没有设定 不能赋值
# print(t.y)
t2 = Test1()
print(t2.__slots__)




# 当一个类需要创建大量实例时，可以通过__slots__声明实例所需要的属性，
#
# 例如，class Foo(object): __slots__ = ['foo']。这样做带来以下优点：
#
# 更快的属性访问速度
# 减少内存消耗

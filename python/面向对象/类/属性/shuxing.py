# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 每一个与类相关联的方法调用都自动传递实参，它是一个指向实例本身的引用，让它实例能够访问类中的属性和方法。
class Dog(object):
    def __init__(self,name,mile):
        self.name = name
        self.mile = mile

    def sit(self):
        print(self.name)

# 通过方法让自身属性进行递增
    def inc(self,mile):
        self.mile += mile

d = Dog("1", 10)
print(d.mile)
d.inc(1)
print(d.mile)
d.inc(2)
print(d.mile)

print("——————————————————————————————————————————————————")

# https://blog.csdn.net/sjyttkl/article/details/80655421
# 属性可以分为两类，一类是Python自动产生的，如__class__，__hash__等，另一类是我们自定义的，如上面的hello，name。我们只关心自定义属性。
# 类和实例对象(实际上，Python中一切都是对象，类是type的实例)都有__dict__属性，里面存放它们的自定义属性(对与类，里面还存放了别的东西)。

class T(object):
    name = 'name'

    @property
    def hello(self):
        return self.name
t = T()
t.name = "name2"
# t.hello = s         #   property不可修改
T.hello = 1
print(T.hello)

print("dir(t)"+str(dir(t)))
print("t.__dict__"+str(t.__dict__))             # 只打印自定义属性


print("——————————————————————————————————————————————————")
print(dir(T))
print(T.__dict__)                               # 除了自定义 还有其他属性
print(T.__dict__['name'])

print(T.name)
print(t.name)


print("——————————————————————————————————————————————————")
print(t.__hash__())
print(hash(t))
print(T.__hash__)
print(hash(T))
print("——————————————————————————————————————————————————")


# Person类很明显能够看出区别，不继承object对象，只拥有了doc , module 和 自己定义的name变量, 也就是说这个类的命名空间只有三个对象可以操作.
# Animal类继承了object对象，拥有了好多可操作对象，这些都是类中的高级特性。


class Person:
    """
    不带object
    """
    name = "zhengtong"


class Animal(object):
    """
    带有object
    """
    name = "chonghong"


if __name__ == "__main__":
    x = Person()
    print "Person", dir(x)

    y = Animal()
    print "Animal", dir(y)
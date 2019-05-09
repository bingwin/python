# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# Python中不存在真正的私有方法。为了实现类似于c++中私有方法，可以在类的方法或属性前加一个“_”单下划线，意味着该方法或属性不应该去调用，它并不属于API。
class Student(object):


    #  _和__外部都不能访问
    def __init__(self, name):
        self.__name = name
        self.__score = 99
        self._te = 1

    def __tet1(self):
        print(1)

    def _tet2(self):
        print(2)

student = Student("Hugh")

# print(student.name)     # 报错
# print(student.score)    # 报错
# print(student.te)       # 报错

# print(student.__tet1)   # 报错
# print(student._tet1)    # 报错

# 这个双下划线更会造成更多混乱，但它并不是用来标识一个方法或属性是私有的，真正作用是用来避免子类覆盖其内容。
# 单划线表示私有 双划线表示受保护

class A(object):
    def __method(self):
        print "I'm a method in A"
    def method(self):
        self.__method()

    def _te(self):
        print("tea")

a = A()
a.method()

class B(A):
    def __method(self):
        print "I'm a method in B"

    def _te(self):
        print("teb")

b = B()
b.method()
b._te()


class CrazyNumber(object):

    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return self.n - other

    def __sub__(self, other):

        return self.n + other
    def __str__(self):
        return str(self.n)

    @staticmethod           # 静态也不可调用
    def __tes1_():
        print(1)

    @classmethod            # 类也不可调用
    def __tes2_(cls):
        print(2)


num = CrazyNumber(10)
print num   # 10
print num + 5   # 5
print num - 20  # 30

# CrazyNumber(10).__tes1__()     # 报错
# CrazyNumber(10).tes1()         # 报错

# num.__tes1_()                  # 报错
# num.tes1()                     # 报错

# CrazyNumber(10).__tes2__()     # 报错
# CrazyNumber(10).tes2()         # 报错


# num.__tes2_()                  # 报错
# num.tes2()                     # 报错
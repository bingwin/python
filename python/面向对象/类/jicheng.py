# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 继承构造函数
import random
import uuid

class Animal(object):
    def __init__(self, name):
        self.name = name


    def tet_1(self):
         self.tet()

    def tet(self):
        pass



class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Doberman', 'German shepherd', 'Beagle'])

        # if self.feed:
        #     accountId = "tet"
        # else:
        #     accountId = str(uuid.uuid1())[:8]

    # % 显示name和thing
    # def fetch(self, thing):
    #     print('%s goes after the %s !' % (self.name, thing))

    @classmethod
    def __fecth__(cls, thing):
        print(thing)

    def tet(self):
        print("tet")



d = Dog('黑皮')
print(d.name)
print(d.breed)
print(d.tet_1())
# d.fetch(1)
del d.name              # 删除实例的name属性
# print(d.name)         # 删除后会报错

print("------------------------------------")



# python可以多继承
# 尽量少用多继承
class Base(object):
    def test(self):
        print("------base")



class A(Base):
    def test1(self):
        print("-----test1")


class B(Base):
    def test2(self):
        print("----test2")

class C(A, B):
    pass

c = C()
c.test1()
c.test2()
c.test()

#类方法和静态方法，使用类名或者实例都可以调用
class ClassA(object):

    # @classmethod
    @staticmethod
    def func_a():
        print('Hello Python')

ClassA.func_a()
# 也可以使用实例调用,但是不会将实例作为参数传入静态方法
ca = ClassA()
ca.func_a()

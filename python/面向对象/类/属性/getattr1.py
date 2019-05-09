# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：

# 要理解 __getattr__ 和 __getattribute__ 的区别：前者只会在待访问的属性缺失时触发，而后者则会在每次访问属性的时候触发

# https://blog.csdn.net/ziteng_du/article/details/78825913

class Student(object):

    def __init__(self):
        self.name = 'Michael'           # 可以不传入值，直接设值

# 调用name属性，没问题，但是，调用不存在的score属性，就有问题了：

s = Student()
print(s.name)
# print(s.score)

print("————————————————————————————————————")


class Student_T(object):

    def __init__(self):
        self.name = 'Michael'          # 所有实例，值一样

    def __getattr__(self, attr):      # 特别合适无结构数据范围，初次执行没有数据，把数据加载进来，再次访问有数据
        if attr == 'score':
            return 99
        # print("getttr1")


s = Student_T()
print(s.name)
print(s.score)
s1 = Student_T()
print(s1.name)
print(s1.score)
print("test")
s.t = 1
print(s.t)


# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。

# setattr自己设定属性和值

print("————————————————————————————————————————————————————————————————")

# python 可以为类附加新的属性值

class Student_S(object):
    def __getattr__(self, item):
        return item + ' is not exits'

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        print("__setattr__")

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        print("__setitem__")

s = Student_S()
print(s.name)  # 调用__getattr__方法 输出'name is not exits'
s.age = 1  # 调用__setattr__ 方法
print(s.age)  # 输出 1
s.name = 'jerry'
print(s.name)
print(s['age'])  # 调用 __getitem__方法 输出1
s['name'] = 'tom'  # 调用 __setitem__ 方法
print(s['name'])  # 调用 __getitem__ 方法 输出 'tom'


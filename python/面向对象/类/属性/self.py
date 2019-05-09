# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
print("小明")

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线，在Python中，实例的变量名如果以开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，
# 所以，我们把Student类改一改：

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        self._te = 1

    def print_score(self):
        print "%s: %s" %(self.__name,self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

student = Student("Hugh", 99)
print(student.get_grade())


# self代表类的实例，而非类

class Test:
    def ppr(self):
        print(self)
        print(self.__class__)

t = Test()
t.ppr()
# 执行结果：
# <__main__.Test object at 0x000000000284E080>
# <class '__main__.Test'>
# ---------------------



# https://blog.csdn.net/CLHugh/article/details/75000104


# python类初始化属性在def __init__()中定义，实例化对象后可直接调用
# python类非初始化属性在def func()中定义，实例化对象后,先调用调用函数，再调用属性

# https://blog.csdn.net/qq_33039859/article/details/79900133
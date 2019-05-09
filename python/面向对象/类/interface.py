# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 首先，我们必须明确的一点是：python里无接口类型，定义接口只是一个人为规定，在编程过程自我约束
# 定义一个接口对继承类进行约束，接口里有什么方法，继承类就必须有什么方法，接口中不能任何功能代码
# Python 中的函数和 Java、C++不太一样，Python 中的函数可以像普通变量一样当做参数传递给另外一个函数
class Interface:

    def f1(self):
        ''' d
        to do something
        :return:
        '''

class Something(Interface):

    def f1(self):
        print('to do something...')

    def f2(self):
        print('to do other..')


# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# https://www.liaoxuefeng.com/wiki/897692888725344/923030547069856


# 使用set，get的调用方法又略显复杂，没有直接用属性这么直接简单。

# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

# 如果一个类已经有实例了，实例又不能销毁，但是新的属性需要有条件，就可以使用@property，赋值的时候就可以进行判断。


class Student(object):

    # def __init__(self, score):                # 类的属性可以不在初始化的时候传入
    #     self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

# s = Student(60)
# print(s.score)

s = Student()
s.score = 60
print(s.score)
# s.score = 999
# print(s.score)

# property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
# 将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的，这种特性的使用方式遵循了统一访问的原则

import math
class Circle:
  def __init__(self, radius):  # 圆的半径radius
      self.radius = radius

  @property
  def area(self):
      return math.pi * self.radius ** 2  # 计算面积

  @property
  def perimeter(self):
     return 2 * math.pi * self.radius  # 计算周长

  def connect(self):
      self.client = self.radius * 2

c = Circle(10)
print(c.radius)
print(c.area)  # 可以向访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值
print(c.perimeter)  # 同上


 # 输出结果:
 # 314.1592653589793
 # 62.83185307179586


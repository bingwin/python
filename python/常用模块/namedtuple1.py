# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# namedtuple
#
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
#
# >>> p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
#
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.x, p.y)

# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
#
# 可以验证创建的Point对象是tuple的一种子类：

print(isinstance(p, Point))
print(isinstance(p, tuple))


# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：

Circle = namedtuple('Circle', ['x', 'y', 'r'])


# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 如果你的代码里，包含的操作(比如检查一个元素是否出现在一个集合中)的频率很高，用set（集合）更合适。

# 通过set()函数或将所有的元素放置在一对大括号内创建一个集合
# 一个集合可以被定义为无序的集合，它是可迭代的，可变的，并且其中不包含重复的元素。
# 1) Collection （集合）每个位置只能保存一个元素(对象)
# 2) Map保存的是"键值对"，就像一个小型数据库。我们可以通过"键"找到该键对应的"值"
Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
Months = {"Jan", "Feb", "Mar"}
Dates = {21, 22, 17}
print(Days)
print(Months)
print(Dates)

# 我们无法访问集合中的单个值。只能如上所示访问所有元素。 但是也可以通过遍历该集合来获取单个元素的列表。

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

for d in Days:
    print(d)


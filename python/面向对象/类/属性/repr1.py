# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# class Item:
#     def __init__(self, name):
#         self.name = name
#
#
# print(Item('aaaaa'))



class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Iiitem({!r})'.format(self.name)

print(Item('aaaaa'))

# 总结：这个函数就是在打印类的时候，控制类输出的字符串。


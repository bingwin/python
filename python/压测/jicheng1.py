# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

class NoticeResult():
    def __init__(self):
        self.name = "name"
        print(2)

    def te2(self):
        self.client.te()

class Clinet():
    def __init__(self, name):
        self.name = name

    def te(self):
        print("te11312")


class Animal(object):
    task_set = NoticeResult()
    def __init__(self, name):
        self.name = name
        self.client = Clinet("11")
        self.client.te()


a = Animal("131241")
# a.task_set.te2()





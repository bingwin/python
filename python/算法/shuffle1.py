# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
import random

list1 = [20, 16, 10, 5]
random.shuffle(list1)
print "随机排序列表 : ",  list1
print("随机排序列表 : ",  list1)
random.shuffle(list1)
print "随机排序列表 : ",  list1
print('随机排序列表:',  list1)
print("随机排序列表")

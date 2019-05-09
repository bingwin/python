# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

def yield_test(n):
    print(n)                        # 函数这里先输出
    for i in range(n):
        yield call(i)
        print("i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")

def call(i):
    return i * 2

# 使用for循环
for i in yield_test(5):
    print(i, ",")





# def test_1():
#     test = {1, 2, 3}
#     for i in test:
#         # print(i)
#         yield i
#         print(10)
#
#
# s = test_1()
# print(s.next())    # 返回一个1，输出一个1
# print(s.next())
# print(s.next())



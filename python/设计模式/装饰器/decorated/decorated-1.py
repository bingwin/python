# -*- coding: utf-8 -*-

# 装饰器本质上python函数，它可以让其他函数在没有任何变动的情况下增加额外功能，装饰器的返回值也是一个函数对象。

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
#
# def ordinary():
#     print("I am ordinary")
#
# pretty = make_pretty(ordinary)
#
# pretty()

# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"and",b)
#       if b == 0:
#          print("Whoops! cannot divide")
#          return
#
#       return func(a,b)
#    return inner
#
# @smart_divide
# def divide(a,b):
#     return a/b
#
# i = smart_divide(divide(2,0))

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

# 以上语法
# @star
# @percent
# def printer(msg):
#     print(msg)
# printer("Hello")

# 相当于以下
def printer(msg):
    print(msg)
printer = star(percent(printer))
printer("Hello")

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

def function(arg,*args,**kwargs):
    print(arg,args,kwargs)

function(6,7,8,9,a=1, b=2, c=3)


# 注意点：参数arg、*args、**kwargs三个参数的位置必须是一定的。必须是(arg,*args,**kwargs)这个顺序，否则程序会报错。
# def function1(arg, **kwargs1, *args):
#     print(arg,kwargs1,args)
#
# function(6 ,a=1, b=2, c=3, 7,8,9,)

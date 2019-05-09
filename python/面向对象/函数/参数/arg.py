# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

#默认参数
def printinfo(name, age=35):
    print "Name: ", name
    print "Age ", age
    return

# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo(name="miki")


# 不定长参数
# 可写函数说明
def printinfo(arg1, *vartuple):
    print "输出: "
    print "arg1:" + str(arg1)
    for var in vartuple:
        print var
    return

# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)





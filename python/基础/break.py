# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# Python break语句，就像在C语言中，打破了最小封闭for或while循环。
# break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
# break语句用在while和for循环中。
# 如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。


for letter in 'Python':  # 第一个实例
    if letter == 'h':
        break
    print '当前字母 :', letter

var = 10  # 第二个实例
while var > 0:
    print '当前变量值 :', var
    var = var - 1
    if var == 5:  # 当变量 var 等于 5 时退出循环
        break

print "Good bye!"


# 当前字母 : P
# 当前字母 : y
# 当前字母 : t
# 当前变量值 : 10
# 当前变量值 : 9
# 当前变量值 : 8
# 当前变量值 : 7
# 当前变量值 : 6
# Good bye!
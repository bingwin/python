# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# Python continue 语句跳出本次循环，而break跳出整个循环。
# continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
# continue语句用在while和for循环中。

for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print '当前字母 :', letter

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print '当前变量值 :', var
print "Good bye!"


# 当前字母 : P
# 当前字母 : y
# 当前字母 : t
# 当前字母 : o
# 当前字母 : n
# 当前变量值 : 9
# 当前变量值 : 8
# 当前变量值 : 7
# 当前变量值 : 6
# 当前变量值 : 4
# 当前变量值 : 3
# 当前变量值 : 2
# 当前变量值 : 1
# 当前变量值 : 0
# Good bye!
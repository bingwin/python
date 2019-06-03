# -*- coding: utf-8 -*-

# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。默认为 -1, 即分隔所有。

str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print str.split()  # 以空格为分隔符，包含 \n
print str.split(' ', 1)  # 以空格为分隔符，分隔成两个

txt = "Google#Runoob#Taobao#Facebook"

# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)

print x

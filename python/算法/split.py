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

# https://www.cnblogs.com/baxianhua/p/8329268.html
# str.split()
#
# 单一分隔符，使用str.split()即可
#
# str.split不支持正则及多个切割符号，不感知空格的数量
#
# re.split()
#
#  多个分隔符，复杂的分隔情况，使用re.split
#
# 原型： re.split(pattern, string, maxsplit=0)
#
# 通过正则表达式将字符串分离。如果用括号将正则表达式括起来，那么匹配的字符串也会被列入到list中返回。maxsplit是分离的次数，maxsplit=1分离一次，默认为0，不限制次数。

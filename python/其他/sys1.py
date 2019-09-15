# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import sys

s = sys.path

c = len(s)  # c=15

for i in range(0, 15):
    print(s[i])

# find / -name site-packages
# /usr/local/lib/python2.7/site-packages
# /Users/huangzetao/venv/lib/python2.7/site-packages
# /Users/huangzetao/Library/Python/2.7/lib/python/site-packages
# /Library/Python/2.7/site-packages  默认pip安装目录库
#
# Library 资源库

# /Users/huangzetao/PycharmProjects/untitled/venv/lib/python2.7/site-packages       # pycharm安装目录
# /Users/huangzetao/venv/lib/python2.7/site-packages
# /Users/huangzetao/.pyenv/versions/3.6.5/lib/python3.6/site-packages
# /Users/huangzetao/.pyenv/versions/3.6.5/envs/ui_autotest_adr/lib/python3.6/site-packages

# DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
# Requirement already satisfied: psutil in /Library/Python/2.7/site-packages (5.6.1)


n = 1

if not n:
    print(1)


# 可以使用encode()函数对字符串进行编码，转换成二进制字节数据，也可用decode()函数将字节解码成字符串；用decode()函数解码

print sys.getdefaultencoding()
s1 = u"中文"
s2 = "中文"
s3 = "zhongwen"
# s4 = s1.encode()
# s5 = s2.encode()
s6 = s3.encode()
s7 = s6.decode()
print(s1)
print(s2)
print(s1, 423)
print(s1, s2, s3)
print(s3)
print(s6)
print(s7)


# 将a（字符串）进行编码，当a为中文时，将Unicode编码为b'\\u4f60\\u597d'，输入b显示时，python自动假设unicode字符的默认编码方式是ASCII，但ASCII中没有b'\\u4f60\\u597d'，所以就直接输出了。
#
# 当a为'hello'时，编码为（也是数字），但print时可以按照ASCII的形式显示bytes类型。

# >> > a = '你好'
# >> > b = a.encode('unicode_escape')
# >> > b
# b'\\u4f60\\u597d'
#
# >> > a = 'hello'
# >> > b = a.encode('unicode_escape')
# >> > b
# b'hello'


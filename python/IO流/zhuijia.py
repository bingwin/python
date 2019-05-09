# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 打开一个文件
# fo = open("foo.text", "w")   # python2使用text不能追加 需要使用txt  多尝试
# print "文件名: ", fo.name
#
# # 关闭打开的文件
# fo.close()

w = file('foo.txt', 'a')
w.write("这里是我新写入的文字内容！！！！\n")
w.close()
r = file('foo.txt', 'r')
str = r.read()
r.close()
print(str)



# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

f_r = open('/Users/huangzetao/Desktop/正式环境.html', 'r')
lines = f_r.readlines()
f_w = open('/Users/huangzetao/Desktop/正式环境.html', 'w')
x = "gray" + '"' + '>' + "未开始测试"
y = "SlateBlue" + '"' + '>' + "测试进行中"
for line in lines:
    if x in line:
        line = line.replace(x, y)
    f_w.write(line)
f_r.close()
f_w.close()


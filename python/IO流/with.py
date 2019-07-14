# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

#关键字with在不再需要访问文件后将关闭。
# with open("text_files/filename.text")as file_object:
# 对与open函数，必须加上as语句,以便获取文件的引用

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
import time
with open('foo.txt', 'rb') as f:
    print(f.read())


with open('foo.txt', mode='r') as f:
    for line in f:
        print(line)
        time.sleep(0.5)

with open('foo.txt', mode='r') as f:
    for line in f:
        print(line, '')
        time.sleep(0.5)

# status
# with open('foo.txt') as f:
#         lines = f.readlines()



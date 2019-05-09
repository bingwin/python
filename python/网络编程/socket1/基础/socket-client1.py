# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
# s.setblocking(0)
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号

s.connect((host, port))
# print s.recv(8)
rep = s.recv(8)                                       # 如果服务器没有发送数据 recv会阻塞后面的进程  使用协程或者用多线程可以实现异步
print(rep)
print(1)
s.send("test1")
print(2)
# t = s.send("test1")
# print(str(t) + "fs")
s.send("test2")
print(3)
s.send("test3")
s.close()

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import time
import socket  # 导入 socket 模块

# s = socket.socket()  # 创建 socket 对象
# host = socket.gethostname()  # 获取本地主机名
# port = 12345  # 设置端口号
#
# s.connect((host, port))

host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号
s = socket.create_connection((host, port), 3)
data = "12"
s.send(data)

# print s.recv(1024)
# t = s.fileno()
# print(t)
# time.sleep(10)
s.close()

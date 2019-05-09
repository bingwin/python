# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# //压测使用 暂时勿动


import socket  # 导入 socket 模块
import time

# s = socket.socket()  # 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setblocking(0)
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(20)  # 等待客户端连接

while True:
    c, addr = s.accept()  # 建立客户端连接
    c.setblocking(0)
    print '连接地址：', addr  # addr是元祖
    # time.sleep(20)
    # c.send('131231241241241241')
    # try:
    test1 = c.recv(8)
    print(test1)

    c.send("11")
    # test2 = c.recv(8)
    # test3 = c.recv(8)
    # print(test1, test2, test3)
    # # except IOError:
    # print(1)
    #
    # c.send("1234")
    # print("test1234")

    # test1 = c.recv(1024)
    # print(test1)

    # test2 = c.recv(8)
    # print(test2)
    # c.close()  # 关闭连接

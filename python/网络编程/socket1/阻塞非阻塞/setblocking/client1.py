# -*- coding:utf-8 -*-


import socket

# 声明协议类型,同时生成socket连接对象
client = socket.socket()

# 链接地址和端口,元组(本地，端口)
client.connect(('127.0.0.1', 12349))

# client.setblocking(False)

i = 0


def send():

    global i
    msg = "test1234"

    # 发送数据 b将字符串转为bys类型
    client.send(msg.encode("utf-8"))

    # 接收服务器端的返回，需要声明收多少，默认1024字节
    id = 1024
    data = client.recv(id).decode()

    # 打印data是recv的data
    print("recv: %s" % data)
    print(i)

    i = i + 1


send()
send()

client.close()

# 关闭接口

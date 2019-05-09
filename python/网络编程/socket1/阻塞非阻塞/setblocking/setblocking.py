# -*- coding:utf-8 -*-


import socket
import time

# 并发操作

server = socket.socket()  # 创建一个socket
server.setblocking(False)  # 设置成非阻塞
server.bind(('127.0.0.1', 12349))
server.listen(5)
print("执行到这， 上面没问题了")

all_connction = []  # 用来存放和连接客户端通信的套接字
while True:
    # 处理用户的连接
    try:
        conn, addr = server.accept()  # 阻塞
        conn.setblocking(False)  # 设置成非阻塞
        print(conn, addr)
        print("{}连接".format(addr))
        all_connction.append(conn)
    except IOError as e:
        pass

    # 处理已经连接的客户的消息
    time.sleep(1)
    for conn in all_connction:
        try:
            data = conn.recv(1024)  # 阻塞
            if data == b'':
                all_connction.remove(conn)
                conn.close()
            else:
                print("接收到的数据: ", data.decode())
                conn.send(data)

        except IOError as e:
            pass

server.close()

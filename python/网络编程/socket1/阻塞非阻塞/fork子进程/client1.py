# -*- coding:utf-8 -*-

import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '127.0.0.1', 12347


def send_message(s, message):
    """ 发送请求 """
    s.sendall(message)


def client():
    message = "Hello, I'm client"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.setblocking(0)
    s.connect(SERVER_ADDRESS)
    send_message(s, message)
    print 'Client is Waiting response...'
    start = time.time()
    data = s.recv(1024)
    end = time.time()
    print("循环运行时间:%.2f秒" % (end - start))
    s.close()
    print 'Client recv:', repr(data)

# 打印从服务器接收回来的数据
if __name__ == '__main__':
    client()



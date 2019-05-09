# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


import time
from socket import socket, AF_INET, SOCK_STREAM
import threading

buffsize = 2048


def tcplink(sock, addr):
    # print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        try:
            # data = sock.recv(buffsize)
            data = sock.recv(buffsize).decode()
            time.sleep(1)
            if data == 'exit' or not data:
                break
            sock.send('Hello, %s!' % data)
        except Exception as e:
            print(str(e))
            break
    sock.close()
    print 'Connection from %s:%s closed.' % addr


def main():
    host = ''
    port = 12345

    ADDR = (host, port)

    tctime = socket(AF_INET, SOCK_STREAM)
    tctime.bind(ADDR)
    tctime.listen(5)

    print('Wait for connection ...')
    while True:
        sock, addr = tctime.accept()
        print 'Accept new connection from %s:%s...' % addr

        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


if __name__ == "__main__":
    main()


# Broken pipe错误原因
# 客户端再发起请求后没有等服务器端相应完，点击了stop按钮，导致服务器端接收到取消请求。
# 通常情况下是不会有这么无聊的用户，出现这种情况可能是由于用户提交了请求，服务器端相应缓慢，
# 比如业务逻辑有问题等原因，导致页面过了很久也没有刷新出来，用户就有可能取消或重新发起请求。
# -*- coding:utf-8 -*-
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '127.0.0.1', 12345
REQUEST_QUEUE_SIZE = 5

def handle_request(client_connection):
    start = time.time()
    request = client_connection.recv(1024)
    # print('Server recv: {request_data}'.format(request_data=request.decode))
    time.sleep(10)  # 模拟阻塞事件
    http_response = "Hello, I'm server"
    client_connection.sendall(http_response)
    end = time.time()
    print(request)
    print("循环运行时间:%.2f秒" % (end - start))

def server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Server on port {port} ...'.format(port=PORT))
    while 1:
        client_connection, client_address = listen_socket.accept()
        handle_request(client_connection)
        client_connection.close()

if __name__ == '__main__':
    server()

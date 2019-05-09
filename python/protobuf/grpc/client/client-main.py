# ! /usr/bin/env python
# -*- coding: utf-8 -*-

# 实现了客户端用于发送数据并打印接收到 server 端处理后的数据


import grpc
import data_pb2
import data_pb2_grpc

_HOST = 'localhost'
_PORT = '8280'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    print(conn)
    client = data_pb2_grpc.FormatDataStub(channel=conn)   # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    print(client)
    response = client.DoFormat(data_pb2.actionrequest(text='hello,world!'))   # 返回的结果就是proto中定义的类
    print("received: " + response.text)

if __name__ == '__main__':
    run()

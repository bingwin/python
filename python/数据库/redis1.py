# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 安装模块: pip3 install redis
# 导入模块：import redis
# 连接方式：
# 严格连接模式：r=redis.StrictRedis(host="",port=)
# 更Python化的连接模式：r=redis.Redis(host="",port=)
# StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令
# Redis与StrictRedis的区别是：Redis是StrictRedis的子类，用于向前兼容旧版本的redis-py，并且这个连接方式是更加"python化"的

# 连接池：
# 为了节省资源，减少多次连接损耗，连接池的作用相当于总揽多个客户端与服务端的连接，当新客户端需要连接时，只需要到连接池获取一个连接即可，实际上只是一个连接共享给多个客户端。

# import redis
#
# pool= redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)
#
# r=redis.Redis(connection_pool=pool)
# r2=redis.Redis(connection_pool=pool)
# r.set('apple','a')
# print(r.get('apple'))
# r2.set('banana','b')
# print(r.get('banana'))
#
# print(r.client_list())
# print(r2.client_list())     # 可以看出两个连接的id是一致的，说明是一个客户端连接

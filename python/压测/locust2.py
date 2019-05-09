# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

from locust import HttpLocust, TaskSet, task
from locust import events
import time
from gevent import socket, monkey

monkey.patch_all()
import gevent


# import gevent
# from gevent import socket, monkey
# monkey.patch_all()
# import time
# import struct

class UserBehavior(TaskSet):

    @task
    def index(self):
        start_time = time.time()

        host = socket.gethostname()  # 获取本地主机名
        port = 12345  # 设置端口号
        s = socket.create_connection((host, port), 30)
        s.sendall("11")

        watcher = gevent.get_hub().loop.io(s.fileno(), 1)
        watcher.start(s.recv(8))

        s.close()
        # s = socket.socket()  # 创建 socket 对象
        # s.connect((host, port))
        # s.send("11")
        total_time = int((time.time() - start_time) * 1000)
        events.request_success.fire(request_type="Request", name="test", response_time=total_time, response_length=0)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "172.17.152.158:12345"
    min_wait = 1000
    max_wait = 2000
# locust -f locust2.py --no-web -c 4 -r 2 -t 3s
# locust -f locust2.py --no-web -c 20 -r 4 -t 10s

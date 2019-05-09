# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

from locust import HttpLocust, TaskSet, task
from locust import events
import time


class UserBehavior(TaskSet):

    # def on_start(self):
    #     self.client.get("/")

    @task
    def index(self):
        start_time = time.time()
        r = self.client.get("/")
        assert r.status_code == 200
        total_time = int((time.time() - start_time) * 1000)
        events.request_success.fire(request_type="Request", name="test", response_time=total_time, response_length=0)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://www.baidu.com"
    min_wait = 1000
    max_wait = 1000

# locust -f locust1.py --no-web -c 100 -r 10 -t 20s
# Hatching and swarming 100 clients at the rate 10 clients/s...
# 以10个客户/秒的速度孵化和聚集100个客户…


# locust -f locust1.py --no-web -c 8 -r 2 -t 5s                             Index 28个请求             Index+onstaet 36个请求
# locust -f locust1.py --no-web -c 4 -r 2 -t 3s

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import requests

r = requests.get('https://www.baidu.com/')         # 豆瓣首页

print(r.status_code)

print(r.text)

# 对于带参数的URL，传入一个dict作为params参数：

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})

print(r.url)   # 实际请求的URL

print(r.encoding)


# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：

# print(r.content)

# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.
#       forecast%20where%20woeid%20%3D%202151330&format=json')
#       响应错误
#
# print(r.json())

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：

# params = {'key': 'value'}
# r = requests.post(url, json=params) # 内部自动序列化为JSON


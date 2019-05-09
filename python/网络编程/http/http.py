# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import requests
import json

def main():
    req = requests.get('http://www.yiibai.com/api/v2/user?id=2')
    print('HTTP Status Code: ' + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print("User name is :"+json_response['username'])

main()

# req = requests.post('http://api/user', data=None, json=None)
# 它与上面的GET请求完全相同，但它有两个额外的关键字参数 -data - 可以填充在一个字典，一个文件或字节，将在POST请求的HTTP正文中传递。json - 可以使用json对象填充，该对象也将在HTTP请求的主体中传递。
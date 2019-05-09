# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 【Python面试真题】- src = “security/afafsff/?ip=123.4.56.78&id=45″，请写一段代码用正则匹配出IP ？

import re

src = "security/afafsff/?ip=123.4.56.78&id=45"

# ip = re.findall(r'ip=\d+.\d+.\d+.\d+', src)         #  我
ip = re.findall(r'ip=\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', src)          # 答案

ip = str(ip[0])
ip = ip[3:]
print(ip)
print(1)
print(ip)

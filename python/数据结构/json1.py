# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
# 不能起名为json.py 导入会报错

import json

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

json2 = json.dumps(data)
print json2

print json.dumps({'a': 'Runoob', 'b': 7}, sort_keys=True, indent=4, separators=(',', ': '))

print("——————————————————————————————————————————————")

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'

text = json.loads(jsonData)
print text


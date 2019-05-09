# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 怎么写一段代码用json数据的处理方式获取{“persons”:[{“name”:”yu”,”age”:”23″},{“name”:”zhang”,”age”:”34″}]}这一段json中第一个人的名字？

import json

j = json.loads('{"persons":[{"name":"yu", "age":"23"}, {"name":"zhang", "age":"34"}]}')
print(j)
print(j.values())
print(j.values()[0][0])
print(j.values()[0][0]['name'])


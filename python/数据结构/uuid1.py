# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

import uuid

# 　　uuid是128位的全局唯一标识符（univeral unique identifier），通常用32位的一个字符串的形式来表现。有时也称guid(global unique identifier)。python中自带了uuid模块来进行uuid的生成和管理工作。（具体从哪个版本开始有的不清楚。。）
#
# 　　python中的uuid模块基于信息如MAC地址、时间戳、命名空间、随机数、伪随机数来uuid。具体方法有如下几个：　　
#
# 　　uuid.uuid1()　　基于MAC地址，时间戳，随机数来生成唯一的uuid，可以保证全球范围内的唯一性。

name1 = uuid.uuid1()
name2 = str(uuid.uuid1())[:8]
name3 = type(name1)
name4 = type(name2)
print(name1)
print(name2)
print(name3)
print(name4)


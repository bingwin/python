
# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
# 不能起名为yaml.py 导入会报错

# YAML可能是所有编程语言中最人性化的数据序列化标准。
# Python yaml模块叫作:pyaml
# YAML是JSON的替代品
# 广泛使用的一个领域是查看/编辑数据结构 - 例如配置文件，调试期间的转储和文档头。

import yaml

mydict = {'a': 2, 'b': 3, 'c': 6}
mylist = [1, 2, 3, 4, 5, 6]
mytuple = ('a', 'b', 'c', 'x', 'y', 'z')

print(yaml.dump(mydict, default_flow_style=False))
print(yaml.dump(mylist, default_flow_style=False))
print(yaml.dump(mytuple, default_flow_style=False))




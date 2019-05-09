# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

class stu():
    name = {}

    def __init__(self, host, accountid=None, password=""):
        self.host = host
        self.accountid = accountid
        self.password = password

    def connected(self):
        self.on_connected(True, "t32")
        self.connected1 = "str"
        print(len(self.connected1))

    def on_connected(self, success=True, exception=None):
        pass


s = stu(1, 2)
print(s.accountid)
print(s.password)  # 输出为空

s = stu(1, 2, 3)
print(s.password)

s = stu(2, password=321)
print(s.accountid)  # 输出为None
print(s.password)

s = stu(1)
print(s.accountid, s.password)

print(type(None))
print(type(""))

s.on_connected()
s.on_connected(True, "t")

# print(s.connected1)
s.connected()

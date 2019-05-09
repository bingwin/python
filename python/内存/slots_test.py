# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# slots_test.py
class Foobar(object):
    __slots__ = ('x')

    def __init__(self, x):
        self.x = x

@profile
def main():
    f = [Foobar(42) for i in range(5)]           # 100MB以上计算缓慢  最低是9MB prfile需要9MB

if __name__ == "__main__":
    main()




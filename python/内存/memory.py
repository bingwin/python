# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 其他信息获取
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000


x = 'bananai1'

for idx in range(0, 8):
    print x[idx], "=", id(x[idx])

# 当运行上面的程序时，将会得到以下输出。 正如可以看到上面的a和指向同一内存位置。N和N也指向相同的位置。


# 1、id(object)返回的是对象的“身份证号”，唯一且不变，但在不重合的生命周期里，可能会出现相同的id值。
# 此处所说的对象应该特指复合类型的对象(如类、list等)，对于字符串、整数等类型，变量的id是随值的改变而改变的。

# 2、一个对象的id值在CPython解释器里就代表它在内存中的地址。(CPython解释器：http://zh.wikipedia.org/wiki/CPython


print("——————————————————————————————————————————————")

class Obj():
    def __init__(self, arg):
        self.x = arg


if __name__ == '__main__':
    obj = Obj(1)
    print id(obj)  # 32754432
    obj.x = 2
    print id(obj)  # 32754432

    s = "abc"
    print id(s)  # 140190448953184
    s = "bcd"
    print id(s)  # 32809848

    x = 1
    print id(x)  # 15760488
    x = 2
    print id(x)  # 15760464

# is与==的区别就是，is是内存中的比较，而==是值的比较

print("——————————————————————————————————————————————")

class Obj():
    def __init__(self, arg):
        self.x = arg

    def __eq__(self, other):
        return self.x == other.x

if __name__ == '__main__':
    obj1 = Obj(1)
    obj2 = Obj(1)
    print obj1 is obj2  # False
    print obj1 == obj2  # True

    lst1 = [1]
    lst2 = [1]
    print lst1 is lst2  # False
    print lst1 == lst2  # True

    s1 = 'abc'
    s2 = 'abc'
    print s1 is s2  # True
    print s1 == s2  # True

    a = 2
    b = 1 + 1
    print a is b  # True

    a = 19998989890
    b = 19998989889 + 1
    print a is b  # False

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

class Quantity(object):                         # python2 需要带object  实例才有其他属性 才会调用_dict_函数 才会调用_set_函数
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        # print(instance.__dict__)
        # print(self.__dict__)
        # print(self.storage_name, value)
        # print(value)
        if value > 0:
            print("test")
            instance.__dict__[self.storage_name] = value        # 当设置为w时，5其实为设置的是self.w = 5   weight就指向了Quantity('w')
            # print(value)                                      # 当设置为weight时，5为self.weight =10   truffle._dict_[self.weight] = 10 会先返回
            # self.__dict__[self.storage_name] = value
        else:
            raise ValueError("must > 0")


class LineItem(object):
    weight = Quantity('weight')
    # weight = Quantity('w')
    price = Quantity('price')
    t1 = Quantity('t')
    t2 = "t2"
    print("1")                                  # 类属性先执行
    def __init__(self, description, weight, price):
        print("1self.weight:" + str(self.weight))
        self.description = description
        print("2self.weight:" + str(self.weight))
        self.weight = weight                        # 设置为weight时，在这里赋值了 后面输出为5
        self.price = price
        print("3self.weight:" + str(self.weight))
        # print(weight)                            # 实例属性后执行

        # if price > 0:                           # 初始化时也可以做判定
        #     self.price = price
        # else:
        #     raise ValueError("must > 0")


    def subtotal(self):
        return self.weight * self.price


print(Quantity.__dict__)
# q = Quantity("q")
# print(dir(q))                                   # 带不带object 表现不同

truffle = LineItem("white", 5, 1)
print(truffle.weight)
# truffle.weight = 20                             #  当为w时， truffle.weight 设置的是 truffle.w
# print("truffle.w:" + str(truffle.w))
# print(truffle.weight)                           # 没有storage_name属性  因为类的weight被实例的属性覆盖了 为20     当设置为"w"时，为Quantity实例。。。？
# print("truffle.w:" + str(truffle.w))
print("test" + str(LineItem.weight))            # 实例weight的地址
print(LineItem.weight.storage_name)             #
print(truffle.t1)
# print(truffle.subtotal())

# t1 = Quantity("t")
# print(t1.__dict__)

print("——————————————————————————————————————————————————")


class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print 'Retrieving', self.name
        return self.val

    def __set__(self, obj, val):
        print 'Updating', self.name
        self.val = val

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

# m = MyClass()
# s1 = m.x
# print(s1)
# m.x = 20
# print(m.x)

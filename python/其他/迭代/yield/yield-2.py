# encoding:UTF-8

# def func():
#    n = 0
#    while 1:
#      n = yield n
#
# f = func()
# f.next()
# f.send(1)
# f.send(2)

# https://blog.csdn.net/mieleizhi0522/article/details/82142856

def foo():
    print("starting...")
    while True:
        # red = 1
        res = yield 4              # 先执行左边 再执行右边    # 传的值就是res
        # print("red:",red)
        print("res:", res)
g = foo()
print(next(g))
print("*"*20)
# print(next(g))

print(g.send(2))

print("————————————————————————————————————————————————————————————————————")

def consumer(name):
    print('begin..')
    while True:
        baozi = yield name  # 第一次执行时返回name的值，然后将send的值赋值给yield
        print('is you %s' %baozi)  # 所以此时baozi的值为1

d = consumer('zhang')
print(d.next())
print(d.next())
print(d.next())
# print(d.send(None))
print(d.send(1))
print(d.send(2))
print(d.send(3))
print(d.send(5))

# begin..
# zhang
# is you 1
# zhang
# is you 2
# zhang
# is you 3
# zhang
# is you 5
# zhang

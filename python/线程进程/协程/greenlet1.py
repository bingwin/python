# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

from greenlet import greenlet

def tes1():
    print 12
    gr2.switch()
    print 34           # 执行完返回主线程
    # gr2.switch()

def tes2():
    print 56
    gr1.switch()
    print 78

print(1)
gr1 = greenlet(tes1)
print(2)
gr2 = greenlet(tes2)
print(3)
gr1.switch()            #  gr1.switch() 恰恰实现了从 main 到 gr1 的跳跃
print(4)

# 这个时候 test1 执行到头了，gr1 的栈里面空了。Greenlet 设计了 parent greenlet 的概念，就是说，当一个 greenlet 的入口函数执行完之后，会自动切换回其 parent。
# 默认情况下，greenlet 的 parent 就是创建该 greenlet 时所在的那个栈，前面的例子中，gr1 和 gr2 都是在 main 里被创建的，所以他们俩的 parent 都是 main。
# 所以当 gr1 结束的时候，会回到 main 的最后一句，接着 main 结束了，所以整个程序也就结束了——78 从来没有被执行到过。另外，greenlet 的 parent 也可以手工设置



print("————————————————————————————————————————————")


import gevent
import time
print(1)
gevent.sleep(3)
print(2)
time.sleep(0.5)
print(3)
time.sleep(0.5)
print(4)



#coding=utf-8
# >>> def gen_example():
#
# ...     print 'before any yield'
#
# ...     yield 'first yield'
#
# ...     print 'between yields'
#
# ...     yield 'second yield'
#
# ...     print 'no yield anymore'
#
# ...
#
# >>> gen = gen_example()
#
# >>> gen.next()　　　　＃ 第一次调用next
#
# before any yield
#
# 'first yield'
#
# >>> gen.next()　　　　＃ 第二次调用next
#
# between yields
#
# 'second yield'
#
# >>> gen.next()　　　　＃ 第三次调用next
#®
# no yield anymore
#
# Traceback (most recent call last):
#
#   File "<stdin>", line 1, in <module>
#
# StopIteratio

def my_gen():
    n = 1
    print('This is printed first, n= ', n)
    yield n

    n += 1
    print('This is printed second, n= ', n)
    yield n

    n += 1
    print('This is printed at last, n= ', n)
    yield n

a = my_gen()
i = next(a)
print(i)
i = next(a)
print(i)
i = next(a)
print(i)

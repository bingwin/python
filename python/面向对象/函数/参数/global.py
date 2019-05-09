# -*- coding: utf-8 -*-


# coding: utf-8

age = 18


def happy_birthday():
    global age                  # 定义为global后，可以使用
    print "age {}, happy birthday ~".format(age)
    age += 1


happy_birthday()

print "your age is {}".format(age)

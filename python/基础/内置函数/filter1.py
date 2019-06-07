#!/usr/bin/python
# -*- coding: UTF-8 -*-

def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)

s = filter(lambda x: x % 2, range(1, 10))
print(s)
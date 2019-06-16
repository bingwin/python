#!/usr/bin/python
# -*- coding: UTF-8 -*-

def is_odd(n):
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(newlist)

s = filter(lambda x: x % 2, range(1, 10))
print(s)


str ="h3110 23 cat 444.4 rabbit 11 2 dog"
int1 = [int(s) for s in str.split() if s.isdigit()]
print(int1)

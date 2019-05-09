# -*- coding: utf-8 -*-

def sort_pri(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)     # sort 按照helper进行排序


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_pri(numbers, group)
print(numbers)

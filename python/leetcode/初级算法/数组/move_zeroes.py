# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。


def moveZeroes(a):
    count = 0
    while 0 in a:                   # 如果remove角标超出 用while
        a.remove(0)
        count += 1
    for i in range(0, count):
        a.append(0)
    return a

if __name__ == "__main__":
    a = [1, 23, 4, 0, 2, 0, 9]
    print(moveZeroes(a))

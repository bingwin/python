# -*- coding: utf-8
# # Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

# 示例 1:

# 输入: [10,2]
# 输出: 210
# 示例 2:

# 输入: [3,30,34,5,9]
# 输出: 9534330
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

# 不是很完美 没有re
def largest_number(a):
    s = ""

    def equal(k, largest):
        for i in range(0, len(largest)):
            if k[i] > largest[i]:
                return 1
            if k[i] < largest[i]:
                return 2
            else:
                continue
        return 0

    def remove_largest(s, a):
        if len(a) == 0:
            print(s)
            return s
        largest = "0"
        for k in a:
            i = str(k)
            if i[0] > largest[0]:
                largest = i
            if i[0] == largest[0]:
                t = equal(i, largest)
                if t == 1 or t == 0:
                    largest = i
        index_1 = a.index(int(largest))
        # print(index_1)
        # print(largest)
        s_largest = str(largest)
        # print(s)
        s = s + s_largest
        del a[index_1]
        remove_largest(s, a)

    remove_largest(s, a)
    return s

if __name__ == "__main__":
    a = [3, 30, 34, 5, 9]
    # a = [1, 4]
    print(largest_number(a))

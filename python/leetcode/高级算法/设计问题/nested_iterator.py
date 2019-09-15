# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
#
# 列表中的项或者为一个整数，或者是另一个列表。
#
# 示例 1:
#
# 输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
# 示例 2:
#
# 输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: [1,4,6]。

l=[]
def nested_iterator(nums):
    for i in nums:
        if type(i) == list:
            self.nested_iterator(i)
        else:
            l.append(i)
    return l


if __name__ == "__main__":
    l1 = [[1, 1], 2, [1, 1]]
    print(nested_iterator(l1))

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# 自己
def length_of_longest_substring(a):
    l = []
    len1 = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i <= j:
                if a[j] not in l:
                    l.append(a[j])
                    # print(l)
                else:
                    if len(l) > len1:
                        len1 = len(l)
                    del l[:]
                    break
    return len1

def del_1(a):
    print(a)
    del a[:]
    print(a)


if __name__ == "__main__":
    b1 = "123345121"
    b2 = "pwwkew"
    a1 = list(b1)
    a2 = list(b2)
    print(length_of_longest_substring(a1))
    print(length_of_longest_substring(a2))

    # print(del_1(a))

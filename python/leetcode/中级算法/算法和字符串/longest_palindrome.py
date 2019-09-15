# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"


def longest_palindromea(a):
    l1 = []
    l2 = []
    l3 = []
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i <= j:
                l1 = a[i:j]
                for k in range(0, len(l1) / 2):
                    if l1[k] == l1[-(k + 1)]:
                        l2.append(l1)
                        break
                    else:
                        break
    # for i in l2:
    #     if len(i) > len(l3):
    #         l3 = i
    return l2


if __name__ == "__main__":
    a = "bababd"
    print(longest_palindromea(a))

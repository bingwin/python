# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.

# 自己
def firstUniqchar(b):
    # a = list(b)
    for i in range(0, len(b)):
        for j in range(0, len(b)):
            if i > j:
                if a[i] == a[j]:
                    break
                else:
                    return a[i]

# 其他
def firstUniqChar(s):
    """
    遍历字符串中的字符，如果满足以下两个条件，则返回idx
    1. 该字符不存在于 s[:idx]
    2. 该字符不存在于 s[idx + 1:]
    :param s:
    :return:
    """
    for idx, c in enumerate(s):
        if c not in s[idx + 1:] and c not in s[:idx]:
            return idx
    return -1

if __name__ == "__main__":
    a = "eedtcode"
    answer = firstUniqchar(a)
    print(answer)

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

# 参考
# def permute(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     res = []
#
#     def back(nums_all, temp):
#         if len(nums_all) == 0:
#             res.append(temp)
#             return
#         for i in range(len(nums_all)):
#             back(nums_all[:i] + nums_all[i + 1:], temp + [nums_all[i]])  # nums_all[:i] + nums_all[i + 1:] 相当于remove了[i]
#
#     t = []
#     back(nums, t)

# 自己
def partition(s):
    res = []

    def backtrack(List, tmp):
        if not List:
            # print(List)
            res.append(tmp)
            return
        for i in range(len(List)):
            if List[:i + 1] == List[i::-1]:  # 判断是不是回文字符串
                # print(List[:i + 1], List[i::-1])
                # print(List[i + 1:], tmp + [List[:i + 1]])
                backtrack(List[i + 1:], tmp + [List[:i + 1]])

    backtrack(s, [])
    return res


if __name__ == "__main__":
    s = "121345"
    print(s[:2], s[2:], s[2::-1], s[::-1])  # 123和321 # 双冒号 反转
    # partition(s)
    print(partition(s))

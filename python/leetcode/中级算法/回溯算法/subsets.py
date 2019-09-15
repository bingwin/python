# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# 自己
# def subsets(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     res = []
#
#     def back(nums_all, temp):
#         if len(nums_all) == temp:
#             res.append(temp)
#             return
#         for i in range(len(nums_all)):
#             temp.sort()
#             if temp not in res:
#                 res.append(temp)
#             back(nums_all[:i] + nums_all[i + 1:], temp + [nums_all[i]])  # nums_all[:i] + nums_all[i + 1:] 相当于remove了[i]
#
#     t = []
#     back(nums, t)
#
#     res.append(nums)
#     return res

# 答案
# 这个题蛮有意思的，可以直接从后遍历，遇到一个数就把所有子集加上该数组成新的子集，遍历完毕即是所有子集

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = [[]]
    for i in range(len(nums)):
        size = len(res)
        for j in range(0, size):
            tmp = list(res[j])              # res每一个元素 res[j]
            tmp.append(nums[i])             # 添加新加的num[i]
            res.append(tmp)
    return res

if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums))

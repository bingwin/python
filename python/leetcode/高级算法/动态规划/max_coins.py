# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。
#
# 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
#
# 求所能获得硬币的最大数量。
#
# 说明:
#
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 示例:
#
# 输入: [3,1,5,8]
# 输出: 167
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#      coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []

    def bacnum(nums_all, temp):
        if len(nums_all) == 0:
            res.append(temp)
            return
        for i in range(len(nums_all)):
            bacnum(nums_all[:i] + nums_all[i + 1:],
                   temp + [nums_all[i]])  # nums_all[:i] + nums_all[i + 1:] 相当于remove了[i]

    t = []
    bacnum(nums, t)

    return res


# 自己 写清楚变量
def max_coins(nums):
    res = permute(nums)
    l = []
    # print(res)
    for single_list in res:
        for num in single_list:
            def back(t, s):
                if len(t) == 0:
                    l.append(s)
                for j in range(0, len(t)):
                    if num == nums[j]:
                        if num == nums[j]:
                            if num[j - 1] is not None:
                                left = num[j - 0]
                            else:
                                left = 1
                            if num[j + 1] is not None:
                                right = num[j - 0]
                            else:
                                right = 1
                            s1 = num * left * right
                            s2 = s + s1
                            t.remove(num)
                            back(t, s2)
            back(single_list, nums)
    return l

if __name__ == "__main__":
    nums = [3, 1, 5, 8]
    print(max_coins(nums))
    # print(permute(num))

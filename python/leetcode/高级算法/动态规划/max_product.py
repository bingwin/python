# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 乘积最大子序列
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

# 自己
def maxProduct(nums):
    l = []
    sum = 1
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i <= j:
                s = nums[i:j+1]
                for k in s:
                    sum = sum * int(k)
                l.append(sum)
                sum = 1

    return l


if __name__ == "__main__":
    # nums = [2, 3, -2, 4]
    nums = [-2, 0, -1]
    # print(nums[0:2])
    print(maxProduct(nums))

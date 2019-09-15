# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:
#
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
# 说明:
#
# 你的解法应该是 O(logN) 时间复杂度的。


# 由于题目假设nums[-1]=nums[n]=-∞。所以，我们从0开始往后遍历元素，如果某个元素大于其后面的元素，则该元素就是峰值元素。（但是它时O(n)，不符合题意）
#
# O(logN)一般考虑二分搜索。有如下规律：
#
# 规律一：如果nums[i] > nums[i+1]，则在i之前一定存在峰值元素
#
# 规律二：如果nums[i] < nums[i+1]，则在i+1之后一定存在峰值元素

# 答案
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid - 1] < nums[mid]:
                # 峰值在 mid 右侧
                left = mid
            else:
                # 峰值在 mid 左侧
                right = mid

        if nums[left] > nums[right]:
            return left
        else:
            return right

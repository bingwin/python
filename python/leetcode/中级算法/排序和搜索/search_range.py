# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]

# 自己 答案不是很对
def search_range(nums, target):
    left = 0
    right = len(nums) - 1

    while left + 1 < right and (nums[left] != target and nums[right] != target):
        mid = (left + right) / 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid

    # and (nums[left] != target or nums[right] != target):
    # return nums[left:right]


# 答案
class Solution(object):
    def helper(self, nums, target, flag):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target or (flag and nums[mid] == target):
                r = mid
            else:
                l = mid + 1
        return l

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_index = self.helper(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        return [left_index, self.helper(nums, target, False) - 1]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    print(nums[2:3])
    print(search_range(nums, 8))

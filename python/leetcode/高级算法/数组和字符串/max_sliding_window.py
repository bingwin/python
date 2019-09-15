# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# 提示：
#
# 你可以假设k总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？

# 自己 三个数相加
# def max_sliding_window(nums, k):
#     l = []
#     s = 0
#     for i in range(0, len(nums) - k +1):
#         for j in range(0, k):
#             s = s + nums[i + j]
#         l.append(s)
#         s = 0
#     return l

# 自己最大值
def max_sliding_window(nums, k):
    l1 = []
    l2 = []
    s = 0
    for i in range(0, len(nums) - k+1):
        for j in range(0, k):
            l1.append(nums[i+j])
        l2.append(max(l1))
    return l2

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(max_sliding_window(nums, 3))

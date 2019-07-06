# -*- coding: utf-8 -*-


# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# temp一直累加的值 如果累加的值小于0 那么重新开始累加(一直加，如果小于0了，重新计算)
# res累加过程的最大值

# 自己
def findMaxSum(num):
    temp = 0
    res = num[0]
    for i in range(0, len(num)):
        temp += num[i]
        if temp > res:
            res = temp
        elif temp < 0:
            temp = 0
    return res


# # 其他
# 你可以理解为思想是动态规划，nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和。
# 如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
     """
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)


if __name__ == "__main__":
    num1 = [1, 2, -1, 4, 5, -2]
    num2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # print(findMaxSum(num1))
    # print(findMaxSum(num2))
    print(maxSubArray(num1))
    print(maxSubArray(num2))



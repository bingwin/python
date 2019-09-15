# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


# 子序列的问题->动态规划。
#
# 使用数组 cell 保存每步子问题的最优解。
# cell[i] 代表含第 i 个元素的最长上升子序列的长度。
# 求解 cell[i] 时，向前遍历找出比 i 元素小的元素 j，令 cell[i] 为 max（cell[i],cell[j]+1)



# 答案
def length_of_lis(nums):
    if nums == []:
        return 0
    cell = [1]
    for i in range(1, len(nums)):
        cell.append(1)
        for j in range(i):
            if (nums[j] < nums[i]):                         # 之前的所有比这个元素小元素，每个元素的最长上升子序列长度再+1
                cell[i] = max(cell[i], cell[j] + 1)         # c[i]是1，一定比1大
    return max(cell)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_lis(nums))

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 递增的三元子序列
# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 数学表达式如下:
#
# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: true
# 示例 2:
#
# 输入: [5,4,3,2,1]
# 输出: false

# 答案
# 循环遍历数组，不断更新数组内出现的最小值与最大值，如果出现的一个大于最大值的数，则表示存在长度为 3 的递增子序列。


def increaing_triplet(nums):
    length = len(nums)
    if length < 3:
        return False
    min_num = float('inf')
    max_num = float('inf')
    for n in nums:
        n = int(n)
        if n < min_num:
            min_num = n
            print(min_num)
        elif min_num < n and n <= max_num:
            max_num = n
            print(max_num)
        elif n > max_num:
            return True

    return False




if __name__ == "__main__":
    a = "1213"
    print(increaing_triplet(a))

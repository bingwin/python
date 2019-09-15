# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

# 自己
def product_except_self(nums):
    s = 1
    for i in nums:
        s = s * i

    for i in range(0, len(nums)):       # 进阶完成
        b = s / nums[i]
        nums[i] = b

    return nums



if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(product_except_self(nums))

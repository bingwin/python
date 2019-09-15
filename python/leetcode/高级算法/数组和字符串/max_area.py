# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2
#
#
#
# 图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为
# 49。
#
#
#
# 示例:
#
# 输入: [1, 8, 6, 2, 5, 4, 8, 3, 7]
# 输出: 49

def max_area(nums):
    a = []
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i < j:
                b = int(min(nums[i], nums[j]))
                a.append(b * (j - i))
    return max(a)


if __name__ == "__main__":
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(nums))

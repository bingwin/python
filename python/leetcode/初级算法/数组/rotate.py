# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 说明:
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。

# 自己
def rotate(a, k):
    # a_len = len(a)
    # print(a_len)
    a_k = len(a) - k
    # print(a_k)
    for i in range(0, a_k):
        print(i)
        a.append(a[i])
    print(a)
    for i in range(0, a_k):
        a.remove(a[0])
    print(a)


# 其他
def rotate_2(nums, k):
    k = k % len(nums)
    print(nums[0:k])
    print(nums[0:-k])           # -k 倒数第4个 0到倒数第4个
    nums[:] = nums[-k:] + nums[0:-k]
    print(nums)


if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # rotate(a, 4)
    rotate_2(a, 4)

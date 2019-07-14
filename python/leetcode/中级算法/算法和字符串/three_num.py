# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 三数之和
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


# 每个人全场问一遍 找自己的配对
def two_num_1(a, target):
    # 时间复杂度 n^2
    l = []
    count = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i < j:
                if a[i] + a[j] == target:
                    l.append([])
                    l[count].append(a[i])
                    l[count].append(a[j])
                    count += 1
    return l


# 每个人向主持人登记自己要找的配对，如果登记时，自己要找的配对已经登记过了，则成功
def two_num_2(a, target):
    # 时间复杂度 2n
    l1 = []
    l2 = []
    count = 0
    for i in a:
        if i in l1:
            l2.append([])
            l2[count].append(i)
            l2[count].append(target - i)
            count += 1
        else:
            l1.append(target - i)
    return l2


def three_num_1(a, target):
    # 时间复杂度 n^3
    l = []
    count = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            for k in range(0, len(a)):
                if i < j < k:
                    if a[i] + a[j] + a[k] == target:
                        l.append([])
                        l[count].append(a[i])
                        l[count].append(a[j])
                        l[count].append(a[k])
                        count += 1
    return l


def three_num_2(a, target):
    # 时间复杂度 n^2
    l1 = []
    l2 = []
    count = 0
    cou = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i < j:
                l1.append([])
                l1[count].append(target - a[i] - a[j])
                l1[count].append(i)
                l1[count].append(j)
                count += 1
        for k in range(0, count):
            if a[i] == l1[k][0]:
                if i != l1[k][1] and i != l1[k][2] and i < l1[k][2]:
                    l2.append([])
                    l2[cou].append(l1[k][0])
                    l2[cou].append(a[l1[k][1]])
                    l2[cou].append(a[l1[k][2]])
                    cou += 1
    return l2


    # return l1


if __name__ == "__main__":
    a = [-1, 2, 3, 4, 1, 0, -2, 1]
    # print(two_num_1(a, 2))
    # print(two_num_2(a, 2))
    # print(three_num_1(a, 0))
    print(three_num_2(a, 0))

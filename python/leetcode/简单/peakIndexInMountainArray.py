# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 如果以下属性成立，我们将数组A称为山峰：
#
# A.length >= 3
# 存在一些0 < i < A.length - 1这样的A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# 鉴于一个绝对是一座山的阵列，返回任何  i 这样的  A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]。
#
# 例1：
#
# 输入：[0,1,0]
# 输出：1
# 例2：
#
# 输入：[0,2,1,0]
# 输出：1

A = [1, 2, 3]

def peakIndexInMountainArray(A):
    i = 0
    count = int(A.__len__())
    for i in range(count):
        if i < count-1:
            if A[i] < A[i+1]:
                i = i + 1
    return 1

# print(A.__len__())
print(peakIndexInMountainArray(A))


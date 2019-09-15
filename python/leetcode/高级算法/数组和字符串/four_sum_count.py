# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
#
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
#
# 例如:
#
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# 输出:
# 2
#
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

# 自己
def four_sum_count(A, B, C, D):
    a = []
    b = []
    count = 0
    for i in A:
        for j in B:
            k = int(i) + int(j)
            a.append(k)
    for i in C:
        for j in D:
            k = int(i) + int(j)
            b.append(k)
    for i in a:
        for j in b:
            if i + j == 0:
                count += 1
    return count


# 答案
# 遍历 A 和 B 所有元素和的组合情况，并记录在 ab_map 中，ab_map 的 key 为两数和，value 为该两数和出现的次数
# 遍历 C 和 D 所有元素和的组合情况，取和的负值判断其是否在 ab_map 中，若存在则取出 ab_map 对应的 value 值，count = count + value
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        ab_map = dict()

        for a in A:
            for b in B:
                ab_map[a + b] = ab_map.get(a + b, 0) + 1

        for c in C:
            for d in D:
                s = -(c + d)
                if s in ab_map:
                    count += ab_map[s]

        return count

if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 1]
    print(four_sum_count(A, B, C, D))

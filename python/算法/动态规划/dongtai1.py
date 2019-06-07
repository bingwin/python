# -*- coding: utf-8 -*-


# 动态规划(dynamic programming)是运筹学的一个分支，是求解决策过程(decision process)最优化的数学方法。
# 把多阶段过程转化为一系列单阶段问题，利用各阶段之间的关系，逐个求解，创立了解决这类过程优化问题的新方法——动态规划。
#
# 使用动态规划特征：
# 1. 求一个问题的最优解
# 2. 大问题可以分解为子问题，子问题还有重叠的更小的子问题
# 3. 整体问题最优解取决于子问题的最优解（状态转移方程）
# 4. 从上往下分析问题，从下往上解决问题
# 5. 讨论底层的边界问题
#
# 动态规划最重要的有三个概念：1、最优子结构 2、边界 3、状态转移方程
#
# 二、走楼梯问题
#
# 有十个台阶，从上往下走，一次只能走一个或两个台阶，请问总共有多少种走法？
#
# 1、最优子结构：我们来考虑要走到第十个台阶的最后一步，最后一步必须走到第八或者第九。不难得到 f(10) = f(9)+f(8)。f(9) = f(8)+f(7)
#
# 2、边界：f(1) = 1, f(2) = 2
#
# 3、状态转移：f(n) = f(n-1) + f(n-2)

def get_count(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return get_count(n - 1) + get_count(n - 2)


print(get_count(10))


# 四、最大子序和
# 核心思想：记录以前一个数结尾的最长子序列的最大值。

def max_subarry(nums):
    m = nums[0]
    tem_m = nums[0]
    pre = nums[0]
    for i in range(1, len(nums)):
        print(i)
        if pre <= 0:                    # 如果之前的和小于0，将之前所加的所的值抛弃，下次计算从新值开始，并判断最新的坐标值是否与之前保存的值所谁更大
            tem_m = nums[i]
            pre = nums[i]
        else:                           # 如果之前的和大于0，需要加上最新的坐标值，加上新的坐标值后与之前比较
            pre += nums[i]
            tem_m += nums[i]
        if tem_m > m:
            m = tem_m
    return m


print(max_subarry([-3, -1, -2, -10]))


# )print("test"
print(max_subarry([1, -2, 3, 5, -3, 2, 2, -1, 5, -3]))


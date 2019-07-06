# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

# 自己
def max_profit(a):
    sum = 0
    start = 0
    end = 0
    for i in range(0, len(a) - 2):
        if i == 0:
            if a[i] < a[i + 1]:
                start = a[i]
        if a[i] > a[i + 1] and a[i + 1] < a[i + 2]:
            start = a[i + 1]
        if a[i] < a[i + 1] and a[i + 1] > a[i + 2]:  # 必须用if 如果用elif 最后一个elif和第二个if匹配，a[2] = 1的start执行了 不会再执行后面的elif
            end = a[i + 1]                           # https://www.cnblogs.com/zdwu/p/8072438.html
            sum = sum + end - start
        elif i == len(a) - 3:
            if a[i + 1] < a[i + 2]:
                end = a[i + 2]
                sum = sum + end - start
    return sum


# 题解
def max_profit_2(prices):
    profit = 0
    for day in range(len(prices) - 1):
        differ = prices[day + 1] - prices[day]              # 3,6,8 3的时候买出 6卖出 再买入 8的时候再卖出
        if differ > 0:
            profit += differ
    return profit


if __name__ == "__main__":
    a1 = [7, 1, 5, 3, 6, 4]
    a2 = [1, 5, 3, 6, 8, 4, 9, 1, 3]
    a3 = [7, 1, 5, 3, 6]
    # b1 = max_profit(a1)
    # print(b1)
    b2 = max_profit(a2)
    b3 = max_profit_2(a2)
    print(b2, b3)
    # b3 = max_profit(a3)
    # print(b3)

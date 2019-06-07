# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 题目：
#
# 0-1背包（ZeroOnePack）: 有N件物品和一个容量为V的背包。（每种物品均只有一件）第i件物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使价值总和最大。
#
# 完全背包(CompletePack)：有N种物品和一个容量为V的背包，每种物品都有无限件可用。第i种物品的费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
#
# 多重背包(MultiplePack)： 有N种物品和一个容量为V的背包。第i种物品最多有n[i]件可用，每件费用是c[i]，价值是w[i]。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。
#
# 分析：
#
# 比较三个题目，会发现不同点在于每种背包的数量，0-1背包是每种只有一件，完全背包是每种无限件，而多重背包是每种有限件。

# 【0-1背包问题】就是物品只能放一次，要么放要么不放。
# 【完全背包问题】物品可以无限放
# 【多重背包问题】有n1个物品a1，n2个物品a2，放进背包里，可以转成0-1背包问题，相当于有重复的a1，a2

import time

__author__ = 'ice'


class goods:
    def __init__(self, goods_id, weight=0, value=0):
        self.id = goods_id
        self.weight = weight
        self.value = value


def knapsack(capacity=0, goods_set=[]):
    # 按单位价值量排序
    goods_set.sort(key=lambda obj: obj.value / obj.weight, reverse=True)
    result = []
    for a_goods in goods_set:
        if capacity < a_goods.weight:
            break
        print(a_goods.id, a_goods.weight, a_goods.value)
        capacity -= a_goods.weight
    # if len(result) < len(goods_set) and capacity != 0:
    #     result.append(goods(a_goods.id, capacity, a_goods.value * capacity / a_goods.weight))
    return result


some_goods = [goods(0, 3, 4), goods(1, 8, 6), goods(2, 6, 3), goods(3, 2, 8), goods(4, 1, 2)]

start_time = time.clock()
res = knapsack(6, some_goods)
end_time = time.clock()
print('花费时间：' + str(end_time - start_time))

# for obj in res:
#     print('物品编号:' + str(obj.id) + ' ,放入重量:' + str(obj.weight) + ',放入的价值:' + str(obj.value), ',')
#     print('单位价值量为:' + str(obj.value / obj.weight))

# 花费时间：2.2807240614677942e-05
# 物品编号:3 ,放入重量:2,放入的价值:8,单位价值量为:4.0
# 物品编号:0 ,放入重量:2,放入的价值:4,单位价值量为:2.0
# 物品编号:4 ,放入重量:1,放入的价值:2,单位价值量为:2.0
# 物品编号:1 ,放入重量:1,放入的价值:0.75,单位价值量为:0.75

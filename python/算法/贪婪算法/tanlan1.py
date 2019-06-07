# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 贪婪算法：
# 每步都采取最优的做法，即每步都选择局部最优解，最终得到的就是全局最优解。
#
# 假设你办了个广播节目，要让全美50个州的听众都收听得到。为此你需要决定在哪些广播台播出。
# 在每个广播台播出都需要支付费用，因此你力图在尽可能少的广播台播出。
# 使用贪婪算法可得到非常接近的解：
# 1、选出这样一个广播台，即它覆盖了最多的未覆盖州，即便这个广播台覆盖了一些一覆盖的州也没有关系；
# 2、重复第一步，直到覆盖了所有的州。

# 要覆盖的州
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 广播台清单
stations = dict()
stations['KONE'] = set(['id', 'nv', 'ut'])
stations['KTWO'] = set(['wa', 'id', 'mt'])
stations['KTHREE'] = set(['or', 'nv', 'ca'])
stations['KFOUR'] = set(['nv', 'ut'])
stations['KFIVE'] = set(['ca', 'az'])

# 最终使用的广播台
final_stations = set()

while states_needed:  # 当还有需要的州未覆盖的时候循环
    best_station = None  # 覆盖了最多未覆盖的州的广播台
    states_covered = set()  # 已经覆盖了的州的集合
    # 遍历所有广播台，找出最佳广播台并且将他的覆盖州加入已覆盖的州的集合
    for station, states_for_station in stations.items():
        # 计算需要覆盖的州和每个广播台覆盖的州的交集
        covered = states_needed & states_for_station
        # 如果交集的州数量比已经覆盖的州的数量多
        if len(covered) > len(states_covered):
            best_station = station  # 最佳广播台更新为这个广播台
            states_covered = covered  # 已覆盖的州更新为交集
    states_needed -= states_covered  # 更新为覆盖的州
    final_stations.add(best_station)  # 更新最终结果

print(final_stations)

# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
print(list1 + list2)
print("list1[::-1]", list1[::-1])           # 反向获取

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
# 列表list相当于 arraylist 可以存放不同的元素
# list元素也可以是另一个list

mot = []
mot.append('11a')
mot.append('22a')
mot.append('32a')
print(mot)
mot.reverse()  # 反转
print(mot)
i = len(mot)
print(i)
print(mot[1])
print(mot[-1])  # -1总是返回第一个元素
mot[2] = 1312  # 更新
print(mot)
del mot[1]  # 删除
print(mot)

# 遍历列表
for i in mot:
    print(i)

# python的一个惯例，如果一个函数对对象进行的时就地改动，那么它就返回None，好让调用者知道传入的参数发生了变动，而且并未产生新的对象.，
# 例如，random,shuffle函数也遵守了这个惯例
print("————————————————————————————————")
li = [3, 4, 5, 67, 8, 10]

s1 = li.sort()              # None
print(s1)
print(li)
li = [3, 4, 5, 67, 8, 10]
s2 = sorted(li)
print(s2)

# Python包含以下函数:
# 序号	函数
# 1	cmp(list1, list2)
# 比较两个列表的元素
# 2	len(list)
# 列表元素个数
# 3	max(list)
# 返回列表元素最大值
# 4	min(list)
# 返回列表元素最小值
# 5	list(seq)
# 将元组转换为列


# 1	list.append(obj)
# 在列表末尾添加新的对象
# 2	list.count(obj)
# 统计某个元素在列表中出现的次数
# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj)
# 将对象插入列表
# 6	list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项
# 8	list.reverse()
# 反向列表中元素
# 9	list.sort(cmp=None, key=None, reverse=False)
# 对原列表进行排序

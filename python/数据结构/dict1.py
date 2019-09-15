# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# Python的字典是一种哈希表类型。它们像Perl中发现的关联数组或散列一样工作，由键值对组成。
# 字典键几乎可以是任何Python数据类型，但通常为了方便使用数字或字符串。另一方面，值可以是任意的Python对象。

# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 键在字典中是唯一的，而值可以不必是唯一的。字典的值可以是任何类型的，但是键必须是不可变的数据类型，例如字符串，数字或元组

# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少
#
# python字典和集合的速度是非常快的，列表比较慢
# dict是典型的空间换时间

dict = {}
dict['one'] = "This is one"
dict[2] = "This is my"

tinydict = {'name': 'maxsu', 'code': 1024, 'dept': 'IT Dev'}

print ("dict['one'] = ", dict['one'])  # Prints value for 'one' key
print ('dict[2] = ', dict[2])  # Prints value for 2 key
print ('tinydict = ', tinydict)  # Prints complete dictionary
print ('tinydict.keys() = ', tinydict.keys())  # Prints all the keys
print ('tinydict.values() = ', tinydict.values())  # Prints all the values
print(tinydict.get('name1', 2))

for i in dict.keys():
    print(i)

# 另一种创建方式
alien1 = {
    'color': 'green',
    'point': '5',
    'jeb': '10',
}

for i in alien1.keys():
    print(i)

# 迭代value
for value in alien1.itervalues():
    print(value)

print("-----------------------------------------------------------------------")

# 同时迭代key和value     如果v对我们没有什么用 可以使用占位符_代替
for k, v in alien1.iteritems():
    print(k)
    print(v)
    i = k, v
    print(i is tuple)  # 虽然输出()，但不是tuple
    print(k, v)
    print k, '=', v

# 字典内置函数&方法
# 1	cmp(dict1, dict2)
# 比较两个字典元素。
# 2	len(dict)
# 计算字典元素个数，即键的总数。
# 3	str(dict)
# 输出字典可打印的字符串表示。
# 4	type(variable)
# 返回输入的变量类型，如果变量是字典就返回字典类型。

# 1	dict.clear()
# 删除字典内所有元素
# 2	dict.copy()
# 返回一个字典的浅复制
# 3	dict.fromkeys(seq[, val])
# 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
# 4	dict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值
# 5	dict.has_key(key)
# 如果键在字典dict里返回true，否则返回false
# 6	dict.items()
# 以列表返回可遍历的(键, 值) 元组数组
# 7	dict.keys()
# 以列表返回一个字典所有的键
# 8	dict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# 9	dict.update(dict2)
# 把字典dict2的键/值对更新到dict里
# 10	dict.values()
# 以列表返回字典中的所有值
# 11	pop(key[,default])
# 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# 12	popitem()
# 随机返回并删除字典中的一对键和值。


print("————————————————————————————————————")

resp = {}


def get_req(seq):
    return resp.get(seq, 0)


req = resp.get(100, 0)
print(req)
print(get_req(1000))

prices = {'A': 2, 'B': 1, 'C': 3}
s = maxprices = sorted(zip(prices.values(), prices.keys()))
print(s)

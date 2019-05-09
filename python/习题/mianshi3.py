# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 【Python面试真题】- Python里如何反序的迭代一个序列 ？
# 如果是一个list, 最快的解决方案是：


list = [1, 2, 3]
list.reverse()
print(list)
# try:
#     for x in list:
#       print(list)
# finally:
#     list.reverse()



# 如果不是list, 最通用但是稍慢的解决方案是：

sequence = "12345"

list = []

for i in range(len(sequence)-1, -1, -1):
    x = sequence[i]
    list.append(x)
s = "".join(list)                           # string.join(seq) 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
print(s)

# 额外
s2 = "1".join(list)
print(s2)
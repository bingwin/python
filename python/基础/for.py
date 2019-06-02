# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。


# 倒序输出
for i in range(2, -1, -1):
    print(i)


for i in range(2, 0, -1):
    print(i)

print("test")

for i in range(3):
    print(i)

#  python 3
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()

# python2
for i in range(1, 10):
    for j in range(1, i + 1):
        print j, "*", i, "=", j * i, "\t",  # \t table对齐
    print("")

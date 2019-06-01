# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

def printMatrix(x):
    print(len(x))
    print(len(x[0]))
    print(x[3][2])
    for i in range(len(x[0])):
        print(x[0][i])
    for i in range(len(x) - 1):
        print(x[i + 1][len(x[0]) - 1])
    for i in range(len(x[0])-1, -1, -1):
        # print(i)
        print(x[len(x[i])][i])

    # for i in range(len(x[0])):
    #     if


b = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]
printMatrix(b)



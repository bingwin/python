# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# 自己
def minNumberInRotateArray(a):
    if len(a) == 0:
        return 0

    if a[0] == 1:
        return 1

    if len(a) > 0:
        for i in range(0, len(a)):
            if a[i] < a[i + 1]:
                i = i + 1
            else:
                break
        return a[i + 1]

a = [4, 5, 1, 2, 3]
a = [3, 4, 5, 1, 2]
print(minNumberInRotateArray(a))

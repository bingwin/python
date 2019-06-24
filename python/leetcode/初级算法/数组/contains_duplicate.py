# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
# 示例 2:
#
# 输入: [1,2,3,4]
# 输出: false
# 示例 3:
#
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true

def containsDuplicate(a):
    for i in range(0, len(a)):
        for s in range(0, len(a) - 1):
            if s >= i:  # 如果不作判断 会出现a[i] = a[1]  a[s] = a[i] 即永远返回Ture
                if a[i] == a[s + 1]:
                    return True
    return False


# 转成list转成set 判断长度


if __name__ == "__main__":
    a = [0, 1, 3, 2, 4]
    answer = containsDuplicate(a)
    print(answer)

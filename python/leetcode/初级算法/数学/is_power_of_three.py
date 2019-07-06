# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例 1:
#
# 输入: 27
# 输出: true
# 示例 2:
#
# 输入: 0
# 输出: false
# 示例 3:
#
# 输入: 9
# 输出: true
# 示例 4:
#
# 输入: 45
# 输出: false
# 进阶：
# 你能不使用循环或者递归来完成本题吗？

def is_power_of_three(a):
    for i in range(1, 10):
        if a == 3**i:
            return True
    return False


if __name__ == "__main__":
    print(is_power_of_three(10))

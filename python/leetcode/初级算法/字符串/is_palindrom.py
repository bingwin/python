# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false
import re

# 自己
def is_palindrom(a):
    a1 = a.lower()
    result = ''.join(re.findall(r'[A-Za-z]', a1))
    for i in range(0, len(result)/2):
        if result[i] == result[-(i+1)]:
            return True
        else:
            return False


if __name__ == "__main__":
    a = "A man, a plan, a canal: Panama"
    b = "race a car"
    c = "abcdef"
    print(is_palindrom(a))
    # print(is_palindrom(b))
    print(is_palindrom(c))

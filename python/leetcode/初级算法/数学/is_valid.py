# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 自己
def is_valid(a):
    left = []
    for i in a:
        if i =="(" or i == "{" or i == "[" :
            left.append(i)
        if i ==")" and left[-1] == "(":
            del left[-1]
        if i =="]" and left[-1] == "[":
            del left[-1]
        if i =="}" and left[-1] == "{":
            del left[-1]
    # print(left)
    if len(left) == 0:
        return True
    else:
        return False




if __name__ == "__main__":
    a = "{}["
    b = "{[]}"
    c = "([)]"
    d = "()[]{}"
    print(is_valid(a))
    print(is_valid(b))
    print(is_valid(c))
    print(is_valid(d))


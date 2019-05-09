# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 你会得到J代表珠宝类型的字符串，S代表你拥有的宝石。每个角色S都是你拥有的一种石头。你想知道你有多少宝石也是珠宝。
#
# 在这些信件J是保证不同，而在所有的字符J和S是字母。字母区分大小写，因此"a"被认为是不同类型的石头"A"。
#
# 例1：
#
# 输入： J =“aA”，S =“aAAbbbb”
#  输出： 3
# 例2：
#
# 输入： J =“z”，S =“ZZ”
#  输出： 0
# 注意：
#
# S并且J将由字母组成，长度最多为50。
# 字符J是不同的

# c = "A"
# list = ["A", "B"]
# if c in list:
#     print(c)

# 字符串也可以迭代
# str = "ABC"
# for c in str:
#     print(c)


def numJewelsInStones(J, S):
    count = 0
    for i in S:
        if i in J:
            count = count + 1
    return count

print(numJewelsInStones("abC", "dasfacCCCC"))

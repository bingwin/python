# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


# 怎么寻找下一个位置呢？ 题目给出我们在第一个位置，问我们能否走到最后一个位置。我第一眼看到题目，我能想到的就是我该如何去寻找我的下一个位置。
#
# 下一个位置必须能够让我们走得更远！

# 答案
# 每次走一步 如果剩余步数等于0则失败 如果a[i]大于原来的剩余步数，则更新剩余步数
def can_jump_1(a):
    step = a[0]
    for i in range(0, len(a)):
        if step == 0:
            return False
        step = int(step) - 1
        step = int(max(step, int(a[i])))
    return True


# 答案
# 如果a[i]大于原来的最大的距离，则最大距离更新，当最大距离小于需要达到的长度时，则失败
def can_jump_2(a):
    n = len(a)
    maxlength = 0
    for i in range(n):
        if maxlength < i:
            return False
        else:
            maxlength = int(max(maxlength, i + int(a[i])))
    return True


if __name__ == "__main__":
    a = "121021"
    b = "1212021"
    print(can_jump_1(a))
    print(can_jump_1(b))
    print(can_jump_2(a))
    print(can_jump_2(b))

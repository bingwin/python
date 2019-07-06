# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。

# 自己
def longest_common_prefix(list):
    # print(list[0][0])
    common = list[0]
    for i in range(1, len(list)):  # print 0,1
        if len(list[i]) < len(common):          # 可能出现common的长度大于list[i]的情况
            common = common[0:len(list[i])]
            for j in range(0, len(common)):
                if common[j] == list[i][j]:
                    continue
                else:
                    common = common[0:j]
                    break
    return common


if __name__ == "__main__":
    list = ["flower", "flows", "flight", "flde312", "f"]
    print(longest_common_prefix(list))

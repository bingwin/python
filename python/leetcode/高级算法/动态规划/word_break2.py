# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
#
# 说明：
#
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：
#
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。


# 答案 先判断是否可以拆分，然后进行回溯
class Solution:
    def wordBreak(self, s, wordDict):
        res = []

        def dfs(s, tmp):
            if not s:
                res.append(" ".join(tmp))
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    dfs(s[i:], tmp + [s[:i]])

        def can_break(s, wordDict):
            n = len(s)
            dp = [False] * n
            for i in range(n):
                if s[:i + 1] in wordDict:
                    dp[i] = True
                    continue

                for j in range(i):
                    if dp[j] and s[j + 1:i + 1] in wordDict:
                        dp[i] = True
                        break
            return dp[-1]

        if can_break(s, wordDict):
            dfs(s, [])
        else:
            return []

        return res

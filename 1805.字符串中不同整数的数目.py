#
# @lc app=leetcode.cn id=1805 lang=python3
#
# [1805] 字符串中不同整数的数目
#

# @lc code=start
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        x = ""
        res = set()
        for o in word:
            if '0' <= o <= '9':
                x += o
            else:
                if x:
                    res.add(int(x))
                    x = ""
        if x:
            res.add(int(x))
        return len(res)
# @lc code=end


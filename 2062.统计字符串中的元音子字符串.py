#
# @lc app=leetcode.cn id=2062 lang=python3
#
# [2062] 统计字符串中的元音子字符串
#

# @lc code=start
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        yuan = ['a', 'e', 'i', 'o', 'u']
        N = len(word)
        
        def check_word(w):
            if len(w) < 5:
                return False
            for o in w:
                if o not in yuan:
                    return False
            for o in yuan:
                if o not in w:
                    return False
            return True
        
        res = 0
        for i in range(N):
            for j in range(i, N):
                if check_word(word[i:j+1]):
                    res += 1
        return res
# @lc code=end


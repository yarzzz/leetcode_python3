#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        ll, rr = 1, n
        while ll < rr:
            mm = int((ll + rr) / 2 + 1)
            if guess(mm) < 0:
                rr = mm - 1
            else:
                ll = mm
        return ll
        
# @lc code=end


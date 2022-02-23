#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ll, rr = 1, n
        now = 0
        res = []
        while ll <= rr:
            if now == 0:
                res.append(ll)
                ll += 1
                if k > 1:
                    now = 1
                    k -= 1
            else:
                res.append(rr)
                rr -= 1
                if k > 1:
                    now = 0
                    k -= 1
        return res
# @lc code=end


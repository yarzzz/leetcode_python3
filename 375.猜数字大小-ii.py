#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#

# @lc code=start
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[999999 for _ in range(n + 2)] for _ in range(n + 2)]
        length = 1
        while length <= n:
            ll = 1
            while ll + length - 1 <= n:
                rr = ll + length - 1
                if length == 1:
                    dp[ll][rr] = 0
                elif length == 2:
                    dp[ll][rr] = ll
                else:
                    mm = ll + 1
                    while mm < rr:
                        dp[ll][rr] = min(dp[ll][rr], max(dp[ll][mm-1]+mm,dp[mm+1][rr]+mm))
                        mm += 1
                ll += 1
            length += 1
        return dp[1][n]
# @lc code=end


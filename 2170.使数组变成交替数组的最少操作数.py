#
# @lc app=leetcode.cn id=2170 lang=python3
#
# [2170] 使数组变成交替数组的最少操作数
#

# @lc code=start

from collections import defaultdict as ddict

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = (ddict(int), ddict(int))
        for i, num in enumerate(nums):
            cnt[i % 2][num] += 1
        max_even = 0
        k_even = -1
        for k in cnt[0]:
            if cnt[0][k] > max_even:
                max_even = cnt[0][k]
                k_even = k
        max_odd = 0
        k_odd = -1
        for k in cnt[1]:
            if cnt[1][k] > max_odd:
                max_odd = cnt[1][k]
                k_odd = k
        if k_even == k_odd:
            max_even2 = 0
            for k in cnt[0]:
                if cnt[0][k] > max_even2 and k != k_even:
                    max_even2 = cnt[0][k]
            max_odd2 = 0
            for k in cnt[1]:
                if cnt[1][k] > max_odd2 and k != k_odd:
                    max_odd2 = cnt[1][k]
            return len(nums) - max(max_even + max_odd2, max_even2 + max_odd)
        return len(nums) - max_even - max_odd
# @lc code=end


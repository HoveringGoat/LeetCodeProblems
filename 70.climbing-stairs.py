#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        map = {}
        i = 2
        map[1] = 1
        map[2] = 2

        while i < n:
            i += 1
            map[i] = map[i-1]+map[i-2]
        return map[n]


        
# @lc code=end


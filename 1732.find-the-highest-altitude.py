#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        currentAlt = 0
        for i in gain:
            currentAlt += i
            if currentAlt > maxAlt:
                maxAlt = currentAlt
        return maxAlt
        
# @lc code=end


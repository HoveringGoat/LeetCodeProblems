#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        c = 0
        for i,v in enumerate(nums):
            if s - v == c*2:
                return i
            c += v
        return -1
        
# @lc code=end


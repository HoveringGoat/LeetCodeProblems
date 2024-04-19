#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create set
        numSet = set()
        for i in nums:
            if i in numSet:
                return True
            numSet.add(i)
        return False
        
# @lc code=end


#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startIndex = -1
        endIndex = -1

        for i,v in enumerate(nums):
            if startIndex == -1:
                if v == target:
                    startIndex = i
                    endIndex = i
                continue
            if v != target:
                break
            endIndex += 1
        
        return [startIndex, endIndex]
            

        
# @lc code=end


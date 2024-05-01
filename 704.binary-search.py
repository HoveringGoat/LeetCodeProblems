#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIndex = 0
        maxIndex = len(nums)-1
        
        found = False
        while minIndex < maxIndex:
            index = int((minIndex+maxIndex)*.5)
            if nums[index] > target:
                maxIndex = index
            elif nums[index] < target:
                minIndex = index
            else:
                return index

        return -1
# @lc code=end


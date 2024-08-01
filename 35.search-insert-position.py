#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search and return index
        min = 0
        max = len(nums)
        guess = 0
        while min<max:
            guess = int((min+max-1)/2)
            if nums[guess] > target:
                max = guess
            elif nums[guess] < target:
                min = guess + 1
            else:
                return guess
        return max
            


        
# @lc code=end


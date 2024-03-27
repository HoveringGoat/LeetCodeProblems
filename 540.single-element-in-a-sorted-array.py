#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-2:
            if nums[i] != nums[i+1]:
                return nums[i]
            i+=2

        # if we never found it its the last value
        return nums[-1]
# @lc code=end


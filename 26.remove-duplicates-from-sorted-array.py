# @before-stub-for-debug-begin
from python3problem26 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # if repeat char move forward to first non repeat and swap with index
        # index will track the "new" list end
        index = 1
        forwardIndex = 0
        last = nums[0]

        while forwardIndex < len(nums):
            if last == nums[forwardIndex]:
                forwardIndex += 1
                continue

            # new char
            nums[index] = nums[forwardIndex]
            last = nums[index]
            forwardIndex += 1
            index += 1
            
        return index
        
# @lc code=end


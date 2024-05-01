# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # keep track of start and end index for potential min subarray
        # if current sum of subarray is less than target increase size by moving
        # endindex to the right
        # if its >= to the target record num of values in it and move the start index +1
        
        startIndex = 0
        endIndex = -1
        currentSum = 0
        minSize = 0

        while endIndex < len(nums) and startIndex < len(nums):
            if currentSum < target:
                endIndex += 1
                if endIndex < len(nums):
                    currentSum += nums[endIndex]
                continue
            else:
                size = endIndex+1 - startIndex
                if minSize == 0 or size < minSize:
                    minSize = size
                currentSum -= nums[startIndex]
                startIndex += 1

        return minSize
        
# @lc code=end


# @before-stub-for-debug-begin
from python3problem962 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        # keep track of each passed number.
        # If we hit a number that is higher than it record how big the width is
        # maybe keep track of active indicies?
        # if new index is higher than any of our current values (aka we update any map values)
        # we can safely ignore that one. It would be a subset of the largest width
        # but keep updating the map value if its >
        
        activeIndexes = []
        maxWidth = 0
        lastValueAdded = 0

        # loop through the array front to back and get all the possible ramp start positions
        for i in range(len(nums)):
            if nums[i] < lastValueAdded or i == 0:
                lastValueAdded = nums[i]
                activeIndexes.append(i)

        # walk through the array in reverse order and look at all the possible ramp end positions
        i = len(nums) - 1
        while i >= 0 and len(activeIndexes) > 0:
            if nums[i] >= nums[activeIndexes[-1]]:
                # max possible length for this index
                # pop it and check if the previous one is also satified
                width = i - activeIndexes.pop()
                if width > maxWidth:
                    maxWidth = width
            else:
                # end point invalid continue
                i -= 1
        
        return maxWidth
# @lc code=end


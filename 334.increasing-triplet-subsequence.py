# @before-stub-for-debug-begin
from python3problem334 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = 0
        j = 0
        k = 0
        # [20,100,10,13,11,12]
        # [i, 0, 0, j, 0, k]
        
        # find k
        # max has to be increased TWICE before we can settle on a k value
        min = nums[0]
        valuesIncreased = 0
        max = None
        kMax = None
        for index, value in enumerate(nums):
            if value > min:
                valuesIncreased += 1
                if max == None or value > max:
                    max = value
            elif value < min:
                min = value
                
            if (valuesIncreased > 2) or (valuesIncreased == 2 and value >= max):
                if kMax == None or value >= kMax:
                    kMax = value
                    k = index

        if k == 0:
            return False
        
        for index, value in enumerate(nums[:k]):
            if value < nums[k]:
                if value >= nums[j] or j == 0:
                    j = index

        for index, value in enumerate(nums[:j]):
            if value < nums[j]:
                if value >= nums[i] or i == 0:
                    i = index

        return nums[i] < nums[j] and nums[j] < nums[k]
            
        
# @lc code=end


# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # lets use a set so we dont accidently duplicate.
        triplets = set()
        for i, iValue in enumerate(nums):
            if i + 2 > len(nums):
                # dont interate higher than the 3rd to last value.
                break
            target = -iValue
            hashset = set()
            for value in nums[i+1:]:
                diff = target - value
                if diff in hashset:
                    t = [iValue, diff, value]
                    t.sort()
                    triplet = tuple(t)
                    triplets.add(triplet)
                    
                if value not in hashset:
                    hashset.add(value)

        return list(triplets)
        
# @lc code=end


# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case
        if len(nums) == 1:
            return [nums]
        
        # recurively call nums on all but the first value
        # we can then update the list to include the first value in every possible position

        # since we're here length of nums > 1 which means we'll always have at least one value out of here.
        subsets = self.permute(nums[1:])
        permutations = []
        for subset in subsets:
            for i in range(len(subset)+1):
                # inset nums[0] in the ith place in subset add to return list
                p = []
                if i > 0:
                    p.extend(subset[:i])
                p.append(nums[0])
                if i < len(subset):
                    p.extend(subset[i:])
                permutations.append(p)
        return permutations
        
        
# @lc code=end


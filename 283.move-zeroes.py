# @before-stub-for-debug-begin
from python3problem283 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if nums[i] == 0:
                # swap with first non-zero value to the right
                found = False
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        found = True
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
                if not found:
                    return

        
# @lc code=end


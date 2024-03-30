# @before-stub-for-debug-begin
from python3problem27 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in range(len(nums)):
            # check if its the value we want to remove.
            # If it is we dont increment or move values
            if (nums[i] == val):
                continue

            # found value we want to rewrite. Move it back in the array to the new "end"
            if n < i:
                # dont bother moving if theyre equal
                nums[n] = nums[i]
            n += 1
        return n
        
# @lc code=end


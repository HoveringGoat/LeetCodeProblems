# @before-stub-for-debug-begin
from python3problem189 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        if k >= l:
            k = k % l
        if k == 0:
            return
        
        temp = nums+nums
        temp = temp[l-k:2*l-k]
        for i in range(l):
            nums[i] = temp[i]
        return
        
# @lc code=end


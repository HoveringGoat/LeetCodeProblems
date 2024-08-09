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
        # double reverse method (no human thinks of this)

        l = len(nums)
        if k >= l:
            k = k % l
        if k == 0:
            return
        
        nums.reverse()
        
        i = 0
        while i < l:
            # if we're in k then swap i and k-i
            # else swap i and l+k-i
            swap = k - i - 1
            if i >= k:
                swap = l + k - i - 1
            if swap <= i:
                if swap >= k:
                    break
                i = k
                continue
            t = nums[i]
            nums[i] = nums[swap]
            nums[swap] = t
            i += 1
        return

        # my method
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


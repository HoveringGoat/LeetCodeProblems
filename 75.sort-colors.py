# @before-stub-for-debug-begin
from python3problem75 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = 0
        color = 0

        # sort by color. Stop at 2 since there are only three possible colors.
        while left < len(nums) and color < 2:
            # check if we already have a 'correct' color sorted here
            if nums[left] == color:
                left += 1
                continue

            # make sure right pointer is set before starting the inner loop
            right = left + 1
            # find each color and swap in-place
            while right < len(nums):
                # found color - swap!
                if nums[right] == color:
                    nums[left], nums[right] = nums[right], nums[left]
                    # inc the left pointer since that position is now locked in
                    left += 1
                right += 1

            # reached the end of the list.
            # color has been sorted. inc color to sort next color
            color += 1
    
# @lc code=end


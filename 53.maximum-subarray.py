# @before-stub-for-debug-begin
from python3problem53 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minIndex = 0
        maxIndex = len(nums)-1
        found = True
        minFound = False
        maxFound = False
        maxSum = nums[0]
        while found or (not maxFound or not minFound):
            found = False
            if maxFound or (not minFound and nums[minIndex] <= nums[maxIndex]):
                # try and find a sub array we can remove from the left side
                sum = 0
                for i in range(minIndex, maxIndex):
                    sum += nums[i]
                    if sum > maxSum:
                        maxSum = sum
                    if sum < 0:
                        found = True
                        minIndex = i + 1
                        break
                if not found:
                    minFound = True
            else:
                sum = 0
                for i in range(maxIndex, minIndex, -1):
                    sum += nums[i]
                    if sum > maxSum:
                        maxSum = sum
                    if sum < 0:
                        found = True
                        maxIndex = i - 1
                        break
                if not found:
                    maxFound = True

        sum = 0
        for i in range(minIndex, maxIndex+1):
            sum += nums[i]

        return max(sum, maxSum)
        
# @lc code=end


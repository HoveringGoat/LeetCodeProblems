# @before-stub-for-debug-begin
from python3problem643 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # keep track of the current sum of the last k values
        # return maxSum/k

        sum = 0
        maxSum = 0
        
        for i in nums[:k]:
            sum += i
        maxSum = sum
        for i in range(len(nums[k:])):
            sum -= nums[i]
            sum += nums[i+k]

            if sum > maxSum:
                maxSum = sum

        return maxSum/k

        
# @lc code=end


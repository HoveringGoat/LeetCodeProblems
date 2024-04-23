# @before-stub-for-debug-begin
from python3problem167 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # solution using O(1) extra memory (binary search)
        lastValue = None
        for index, value in enumerate(numbers):
            if lastValue == value:
                # skip if we've already searched this value
                continue
            lastValue = value
            diff = target - value

            # search for diff
            diffMin = index+1
            diffMax = len(numbers)-1
            while(diffMin<=diffMax):
                #search
                diffTarget = int((diffMin+diffMax)*.5)
                if numbers[diffTarget] > diff:
                    diffMax = diffTarget-1
                elif numbers[diffTarget] < diff:
                    diffMin = diffTarget+1
                else:
                    #found
                    return [index+1, diffTarget+1]
        return []

        # solution using O(n) extra memory (map)
        map = {}
        for index, value in enumerate(numbers):
            diff = target - value
            if diff in map:
                return [map[diff], index+1]
            if value not in map:
                map[value] = index+1
        return []
        
# @lc code=end


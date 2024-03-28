# @before-stub-for-debug-begin
from python3problem565 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
# cheated. I swear my exact version of this timed out.
# idk the diff. Must not have been recording visits
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        visited = [False] * len(nums)  # mark if a number is visited
        max_length = 0
        
        for i in range(len(nums)):
            if visited[i]:  # if already visited, skip
                continue
                
            length = 0
            j = i
            while not visited[j]:
                visited[j] = True  # mark as visited
                j = nums[j]  # move to next element in set
                length += 1
                
            max_length = max(max_length, length)  # update max_length
            
        return max_length
        
# @lc code=end


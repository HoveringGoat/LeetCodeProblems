# @before-stub-for-debug-begin
from python3problem128 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfSets = []
        for i in nums:
            foundSet = None
            for s in setOfSets:
                # duplicate value
                if i in s:
                    foundSet = s
                    break
                if i+1 in s or i-1 in s:
                    if foundSet == None:
                        foundSet = s
                    else:
                        # merge sets
                        mergedSet = foundSet.union(s)
                        setOfSets.remove(foundSet)
                        setOfSets.remove(s)
                        setOfSets.append(mergedSet)
                        break
                    s.add(i)
            if foundSet == None:
                newSet = {i}
                setOfSets.append(newSet)
            
        max = 0
        for s in setOfSets:
            if len(s) > max:
                max = len(s)

        return max
        
# @lc code=end


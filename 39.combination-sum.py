# @before-stub-for-debug-begin
from python3problem39 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 1:
            return []
        
        targetCombinations = []
        for i in range(len(candidates)-1, -1, -1):
            newTarget = target - candidates[i]
            if newTarget > 1:
                for l in self.combinationSum(candidates[:i+1], newTarget):
                    l.append(candidates[i])
                    targetCombinations.append(l)
            elif newTarget == 0:
                targetCombinations.append([candidates[i]])

        return targetCombinations

        
# @lc code=end


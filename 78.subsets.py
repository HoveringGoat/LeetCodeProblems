#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subSets = set()
        subSets.add(([]))

        for value in nums:
            # each time we add value to each set and add those back to the sets
            newSets = set()
            for s in subSets:
                s.append(value)
                newSets.add((s))
            for s in newSets:
                subSets.add(s)
        return subSets
        
# @lc code=end


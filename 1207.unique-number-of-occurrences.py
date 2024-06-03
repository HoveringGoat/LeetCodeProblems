#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # convert to dict
        # ensure list of values is a set of length keys
        map = {}
        for i in arr:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        instancesSet = set(map.values())


        return len(instancesSet) == len(map.keys())
        
# @lc code=end


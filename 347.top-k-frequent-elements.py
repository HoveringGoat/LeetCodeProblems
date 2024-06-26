#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {i: nums.count(i) for i in nums}
        
        sortedMap = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))
        topValues = list(sortedMap.keys())

        return topValues[:k]
        
# @lc code=end
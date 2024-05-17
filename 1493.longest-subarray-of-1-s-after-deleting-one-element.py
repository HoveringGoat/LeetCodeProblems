#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max = 0
        lastZeroIndex = None
        startIndex = 0

        for i,v in enumerate(nums):
            if v == 0:
                if lastZeroIndex != None:
                    startIndex = lastZeroIndex + 1
                lastZeroIndex = i
                l = i - startIndex
                if l > max:
                    max = l
                continue
            # its a 1
            l = i - startIndex
            if l > max:
                max = l

        return max
        
# @lc code=end


# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        map = {}
        substringLength = 0
        substringStartIndex = 0

        for index, value in enumerate(s):
            if value in map:
                # get a substring that should be removed
                subStringToRemove = s[substringStartIndex:map[value]+1]
                l = len(subStringToRemove)
                substringLength -= l
                substringStartIndex += l

                for i in subStringToRemove:
                    del map[i]
            
            map[value] = index
            substringLength += 1
            if substringLength > max:
                max = substringLength


        return max
        
# @lc code=end


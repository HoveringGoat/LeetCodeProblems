# @before-stub-for-debug-begin
from python3problem28 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        s = haystack.split(needle)

        # edge case #1
        # needle is not in haystack
        if len(s) == 1:
            return -1
        
        # general case
        # needle is somewhere in haystack
        return len(s[0])
        
            
        
# @lc code=end


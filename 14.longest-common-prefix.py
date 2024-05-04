# @before-stub-for-debug-begin
from python3problem14 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def getCommonPrefix(self, s1: str, s2: str) -> str:
        s = ""
        l = min(len(s1), len(s2))
        for i in range(l):
            if s1[i] == s2[i]:
                s+=s1[i]
                continue
            break
        return s

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        # get common prefix of first two words. get common prefix of that prefix plus next word. repeat
        for s in strs[1:]:
            prefix = self.getCommonPrefix(prefix, s)
            if prefix == "":
                break
        return prefix
        
# @lc code=end


# @before-stub-for-debug-begin
from python3problem242 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # basically count the letters and make sure each one has the same.
        return self.isQuickAnagram(s, t) and (self.buildDict(s) == self.buildDict(t))

    # a quick sanity check (not conclusive (probably))
    def isQuickAnagram(self, s: str, t:str) -> bool:
        return (len(s) == len(t)) and (self.calcAscii(s) == self.calcAscii(t))
        
        
    def calcAscii(self, s:str) -> int:
        i=0
        for c in s:
            i+=ord(c)
        return i
    
    def buildDict(self, s: str) -> dict:
        t = {}
        for c in s:
            if c in t:
                t[c] += 1
            else:
                t[c] = 1
        return t
        
# @lc code=end


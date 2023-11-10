#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # basically count the letters and make sure each one has the same.
        return (len(s) == len(t)) and (self.buildDict(s) == self.buildDict(t))

    def buildDict(self, s: str) -> dict:
        t = {}
        for c in s:
            if c in t:
                t[c] += 1
            else:
                t[c] = 1
        return t
        
# @lc code=end


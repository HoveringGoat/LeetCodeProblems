#
# @lc app=leetcode id=2124 lang=python3
#
# [2124] Check if All A's Appears Before All B's
#

# @lc code=start
class Solution:
    def checkString(self, s: str) -> bool:
        foundB = False
        for char in s:
            if foundB and char == 'a':
                return False
            if char == 'b':
                foundB = True
        return True
# @lc code=end


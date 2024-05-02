#
# @lc app=leetcode id=2399 lang=python3
#
# [2399] Check Distances Between Same Letters
#

# @lc code=start
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        chars = set()
        for index, c in enumerate(s):
            if c in chars:
                continue
            
            value = ord(c)-97
            if s[index + value] != c:
                return False
            chars.add(c)
        return True
        
# @lc code=end


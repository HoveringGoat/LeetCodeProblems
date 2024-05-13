#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # trivial case
        if len(s) == 0:
            return True
        
        n = 0
        for c in t:
            if c == s[n]:
                # found nth char in s in t.
                n += 1
                if n == len(s):
                    # thats all of em!
                    return True
                
        # didnt find em all
        return False
                

        
# @lc code=end


#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        modified = []
        skipCounter = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == "*":
                skipCounter += 1
                continue
            if skipCounter > 0:
                if skipCounter > i:
                    break
                skipCounter -= 1
                continue
            modified.append(s[i])

        modified.reverse()
        return "".join(modified)
        
# @lc code=end


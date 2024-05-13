# @before-stub-for-debug-begin
from python3problem44 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # base case
        if s == p:
            return True
        
        patternIndex = 0
        for i,v in enumerate(s):
            if p[patternIndex] == "?":
                patternIndex +=1
                if patternIndex == len(p):
                    return i == len(s) -1
                continue

            if p[patternIndex] == "*":
                while(patternIndex < len(p) and p[patternIndex] == "*"):
                    patternIndex +=1

                # if this is the last of it we are done too
                if patternIndex == len(p):
                    return True
                found = False
                
                # recursivly call main solve on smaller and smaller subsets of the string
                # if ANY suceed then we can return true
                j = i
                while not found and j < len(s):
                    found = self.isMatch(s[j:], p[patternIndex:])
                    if found:
                        return True
                    
                return found
            
            # nonspecial pattern char
            if v != p[patternIndex]:
                return False
            patternIndex +=1
            if patternIndex == len(p):
                return i == len(s) -1

        return False
            

        
# @lc code=end


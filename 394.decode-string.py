# @before-stub-for-debug-begin
from python3problem394 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        # process string. If we encounter a digit add to digit string and continue
        # if we encounter an open bracket we pass in the rest of the string recursively
        # if we encounter a closed bracket we must be in a recursively called method and
        # can return the current string in the brackets
        # otherwise we just have some chars we can add to the return string
        # we take the result from the recursively called decode string and mult it with 
        # the value in the intString to get the decoded string
        # calling decodeString recursively makes it so we dont have to consider WHAT
        # is in the brackets. Just decode it and return it. If its just chars it'll
        # handle it. If its encoded it'll handle that too! (and make its own calls)

        intString = ""
        returnString = ""
        i = 0

        while i < len(s):
            v = s[i]

            if v.isdigit():
                intString += v

            elif v == "[":
                values = self.decodeString(s[i+1:])
                returnString += int(intString) * values[0]
                intString = ""
                i += values[1]
            
            elif v == "]":
                return (returnString, i+1)
                
            else:
                returnString += v
            
            i += 1
            
        return returnString
        
# @lc code=end


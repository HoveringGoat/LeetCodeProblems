# @before-stub-for-debug-begin
from python3problem5 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def longestPalindrome(self, s: str) -> str:
        # if the whole string is a palindrome return the whole string
        if self.isPalindrome(s):
            return s
        
        maxSubString = ""
        for index, value in enumerate(s):

            # check both even and odd palindromes
            for i in range(2):
                leftIndex = index
                rightIndex = index
                rightIndex += i
                if rightIndex > len(s) - 1:
                    continue
                subString = s[leftIndex:rightIndex+1]
                isPalindrome = self.isPalindrome(subString)

                while isPalindrome:
                    if len(subString) > len(maxSubString):
                        maxSubString = subString
                    leftIndex -= 1
                    rightIndex += 1

                    # ensure we're in bounds
                    if leftIndex < 0:
                        break
                    if rightIndex > len(s) - 1:
                        break
                    subString = s[leftIndex:rightIndex+1]
                    isPalindrome = self.isPalindrome(subString)
            
        return maxSubString
        
# @lc code=end


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
        startIndex = 0
        length = len(s)

        # search all possible subsets from largest to smallest
        for l in range(length, 0, -1):
            for i in range(0, len(s)-l+1):
                subset = s[i:i+l+1]
                if self.isPalindrome(subset):
                    return subset
        
# @lc code=end


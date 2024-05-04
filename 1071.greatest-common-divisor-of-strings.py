# @before-stub-for-debug-begin
from python3problem1071 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def getDivisors(self, s: str):
        divisors = set()
        divisors.add("")
        l = len(s)
        for i in range(1, l+1):
            # split string into i groups
            subStringLength = l/i
            if subStringLength != int(subStringLength):
                continue
            subStringLength = int(subStringLength)
            # check if all substrings are identical
            lastSubstring = s[0:subStringLength]
            subStringIndex = 1
            isDivisor = True
            while subStringLength*(subStringIndex+1) <= l:
                substring = s[subStringLength*subStringIndex:subStringLength*(subStringIndex+1)]
                if substring != lastSubstring:
                    isDivisor = False
                    break
                subStringIndex += 1
            
            if isDivisor:
                divisors.add(lastSubstring)
        return divisors



    def gcdOfStrings(self, str1: str, str2: str) -> str:

        str1D = self.getDivisors(str1)
        str2D = self.getDivisors(str2)

        commonDivisors = []

        for d in str1D:
            if d in str2D:
                commonDivisors.append(d)
        commonDivisors.sort(reverse=True)

        return commonDivisors[0]
        
# @lc code=end


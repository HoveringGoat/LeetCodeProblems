# @before-stub-for-debug-begin
from python3problem443 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        lastChar = chars[0]
        lastCharIndex = 0
        for i in range(len(chars)+1):
            if i < len(chars) and chars[i] == lastChar:
                continue

            # new char found.
            l = i - lastCharIndex
            chars[index] = lastChar
            index += 1
            if l > 1:
                for c in str(l):
                    chars[index] = c
                    index += 1

            if i < len(chars):
            # reset index/last char
                lastChar = chars[i]
                lastCharIndex = i
        
        return index

            




        
# @lc code=end


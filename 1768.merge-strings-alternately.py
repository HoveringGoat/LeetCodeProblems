#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        index = 0
        
        while index < len(word1) and index<len(word2):
            merged += word1[index]
            merged += word2[index]
            index += 1

        if index < len(word1):
            # add rest of word1 to merged word
            merged += word1[index:]

        if index < len(word2):
            # add rest of word2 to merged word
            merged += word2[index:]

        return merged

        
# @lc code=end


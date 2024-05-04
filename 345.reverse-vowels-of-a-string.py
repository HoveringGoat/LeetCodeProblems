#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        reversedVowels = ""
        # create a set of all vowels.
        # read through string and pick out all chars that are vowels
        # creating a new string of just the vowels
        # reverse vowel string
        # read through string again and instead of recording vowels overwrite them with reversed vowl string


        # v2 keep two pointers and start at the start and end of the string
        # move them each in until they encounter a vowel.
        # if leftindex < rightindex swap the chars
        
        # both solutions are O(n) but the second should be moderately faster

        return reversedVowels

        
# @lc code=end


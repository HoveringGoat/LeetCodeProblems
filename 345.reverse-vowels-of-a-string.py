#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # v2 keep two pointers and start at the start and end of the string
        # move them each in until they encounter a vowel.
        # if leftindex < rightindex swap the chars
        
        # both solutions are O(n) but this one should be moderately faster

        # this one probably would be faster if i could do it in place but strings are immutable so we have to
        # recreate the string
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        l = 0
        r = len(s)-1
        leftStr = ""
        rightStr = ""

        while l < r:
            if s[l] not in vowels:
                leftStr += s[l]
                l += 1
                continue
            
            if s[r] not in vowels:
                rightStr = s[r] + rightStr
                r -= 1
                continue

            rightStr = s[l] + rightStr
            leftStr += s[r]
            
            r -= 1
            l += 1

        if l == r:
                leftStr += s[l]

        vowelsReversed = leftStr + rightStr

        return vowelsReversed
    
        # create a set of all vowels.
        # read through string and pick out all chars that are vowels
        # creating a new string of just the vowels
        # reverse vowel string
        # read through string again and instead of recording vowels overwrite them with reversed vowl string
        reversedVowels = ""
        v = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for i in s:
            if i in vowels:
                v.append(i)
        
        for i in s:
            if i in vowels:
                reversedVowels += v.pop()
            else:
                reversedVowels += i

        return reversedVowels

        
# @lc code=end


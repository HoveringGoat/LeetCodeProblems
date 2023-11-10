# @before-stub-for-debug-begin
from python3problem49 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #well we already have an anagram detector. Just uhh try the words together
        modifiedInput = []
        #build value map
        for word in strs:
            a = self.Word()
            a.value = word
            a.asciiValue = self.calcAscii(word)
            a.dictValue = self.buildDict(word)
            modifiedInput.append(a)

        # anagrams should always be next to each other now
        modifiedInput.sort(key=lambda x: x.asciiValue)

        output = []
        sublist = []

        terminatingWord = self.Word()
        terminatingWord.asciiValue = -1
        modifiedInput.append(terminatingWord)
        i = 1
        for currentWord in modifiedInput:
            # terminating condition
            if (currentWord.asciiValue == -1):
                continue

            sublist.append(currentWord)
            if (currentWord.asciiValue != (modifiedInput[i]).asciiValue):
                # we're in a new "group" of anagrams 
                output.extend(self.getAnagrams(sublist))
                sublist = []
            i += 1
        return output
    

    def getAnagrams(self, words):
        output = []
        i = 0
        for word in words:
            i += 1
            # make sure we didnt snag this word already
            # (could probably pop from the input list instead)
            if word.isAnagram:
                continue
            anagrams = [word.value]
            # check all the words after this one
            for w in words[i:]:
                if w.isAnagram:
                    continue
                # get ALL words that are an anagram in this group
                if word.dictValue == w.dictValue:
                    anagrams.append(w.value)
                    w.isAnagram = True
            output.append(anagrams)
        return output
    
    class Word:
        value = ""
        asciiValue = 0
        dictValue = {}
        isAnagram = False

    def calcAscii(self, s:str) -> int:
        i=0
        for c in s:
            i+=ord(c)
        return i
            
    def buildDict(self, s: str) -> dict:
        t = {}
        for c in s:
            if c in t:
                t[c] += 1
            else:
                t[c] = 1
        return t
        
# @lc code=end


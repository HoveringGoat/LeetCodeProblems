# @before-stub-for-debug-begin
from python3problem30 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # we have some string "s" that contains some number of substrings consisting of exact concatinations of list "words"
        # find all starting indicies of these substrings
        # so we want to walk through the string s and check if thats the start of one of the substrings.
        # since all words are the same length we can chop out the expected word size and check if the word matches.
        # if we have a match start going through the rest of the substring making sure we get one instance of each
        # if we do then record the start index to some list and go back to the start position and continue looking
        # char by char
        # we can also end when there isnt enough room to complete another substring len(words)*length of word

        indicies: List[int] = []
        word_length: int = len(words[0])
        substring_length: int = len(words) * word_length
        max_index = len(s) + 1 - substring_length

        for i in range(max_index):
            substring: str = s[i:i+substring_length]
            if self.checkSubString(substring, words.copy()):
                indicies.append(i)
        return indicies
    def checkSubString(self, substring: str, words:List[str]) -> bool:
        word_length: int = len(words[0])
        #print(f"substring: {substring}")
        for i in range(len(words)):
            word = substring[i*word_length:(i+1)*word_length]
            if word not in words:
                #print(f"word: {word} does not exist")
                return False
            #print(f"word: {word} exists")
            words.remove(word)
        return True

        
# @lc code=end


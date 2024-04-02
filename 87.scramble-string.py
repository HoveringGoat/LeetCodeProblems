# @before-stub-for-debug-begin
from python3problem87 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    masterAnagrams = {} 
    masterScrambles = {}

    def isScramble(self, s1: str, s2: str) -> bool:

        # couple trivial cases
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if s1[::-1] == s2:
            return True
        
        if (s1+","+s2) in self.masterScrambles:
            return True
        
        print(len(s1))
        
        def scramble(self, substring: str, index:int) -> bool:
            # check if we have found it
            l = index + len(substring)
            a = s2[index:l]
            if a == substring:
                return True
            elif len(substring) == 1:
                return False
            
            # check possible substring permutations
            for i in range(1, len(substring), 1):
                sub1 = substring[:i] # left substring
                sub2 = substring[i:] # right substring
                l = index + len(sub1)
                a = s2[index:l]
                # check if left half is a scramble of the same portion of s2
                if Solution.isScramble(self, a, sub1):
                    a = s2[l:l+len(sub2)]
                    # check if right half is a scramble of the same portion of s2
                    if Solution.isScramble(self, a, sub2):
                        return True
                    
                    
                l = index + len(sub2)
                a = s2[index:l]
                # check if left half is a scramble of the opposite portion of s2
                if Solution.isScramble(self, a, sub2):
                    a = s2[l:l+len(sub1)]
                    # check if right half is a scramble of the opposite portion of s2
                    if Solution.isScramble(self, a, sub1):
                        return True
                
            return False
        

        # walk through and create a dict of the chars in each string.
        # check if the dicts are equal
        dict1 = {}
        dict2 = {}

        if s1 in self.masterAnagrams:
            dict1 = self.masterAnagrams[s1]
        else:
            for i in s1:
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1
            self.masterAnagrams[s1] = dict1
        
        if s2 in self.masterAnagrams:
            dict2 = self.masterAnagrams[s2]
        else:
            for i in s2:
                if i in dict2:
                    dict2[i] += 1
                else:
                    dict2[i] = 1
            self.masterAnagrams[s2] = dict2
        
        if dict1 != dict2:
            return False
        
        # trim em before doing the brute.
        # we cannot assume the bits trimmed are not moved around

        # i = 0
        # while i < len(s1)-1:
        #     if s1[i] == s2[i]:
        #         i += 1
        #         continue
        #     break
        # if i > 0:
        #     s1 = s1[i:]
        #     s2 = s2[i:]
            
        # i = len(s1) - 1
        # while i >= 0:
        #     if s1[i] == s2[i]:
        #         i -= 1
        #         continue
        #     break
        # if i < len(s1) - 1:
        #     s1 = s1[:i+1]
        #     s2 = s2[:i+1]

        # brute force check all the permutations
        # if one of the permutations leads to invalid solutions skip all of em
        # if we find s2 then return true

        # perform brute scramble 
        # i is the index to cut


        # submit base string and location to cut
        # recursively call function on each subsection passing in modified string
        # if we hit an "end" condition where we cannot cut the string anymore 
        # then we have ONE possible interation of the s2 string. 
        # we can compare them and see if theyre a match. If we ever find a match we can
        # return true

        result = scramble(self, s1, 0)
        if len(s1) == 27:
            a = "neet"
        if result:
            self.masterScrambles[(s1+","+s2)] = True
        return result


        
# @lc code=end


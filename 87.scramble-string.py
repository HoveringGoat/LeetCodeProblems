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
    masterScrambles = {} 
    def isScramble(self, s1: str, s2: str) -> bool:

        # couple trivial cases
        if s1 == s2:
            return True
        if s1[::-1] == s2:
            return True
        
        def scramble(self, substring: str, restStringLeft: str, restStringRight: str) -> bool:
            # check if we have found it
            if len(substring) == 1:
                a = s2[len(restStringLeft)]
                return a == substring

            
            # ensure the rest of string right matches
            if len(restStringRight) > 0:
                a = s2[-len(restStringRight):]
                if Solution.isScramble(self, a, restStringRight) == False:
                    return False
                
            # ensure the rest of string left matches
            if len(restStringLeft) > 0:
                a = s2[:len(restStringLeft)]
                if Solution.isScramble(self, a, restStringLeft) == False:
                    return False
                
            # check possible substring permutations
            for i in range(1, len(substring), 1):
                sub1 = substring[:i] # left substring
                sub2 = substring[i:] # right substring
                foundSub1 = False
                foundSub2 = False

                # no flip check further permutation in left substring
                if scramble(self, sub1, restStringLeft, sub2+restStringRight):
                    foundSub1 = True
                # flip check further permutation in left substring
                elif scramble(self, sub1, restStringLeft+sub2, restStringRight):
                    foundSub1 = True
                
                # no flip check further permutation in right substring
                if scramble(self, sub2, restStringLeft+sub1, restStringRight):
                    foundSub2 = True
                # flip check further permutation in right substring
                elif scramble(self, sub2, restStringLeft, sub1+restStringRight):
                    foundSub2 = True
                    
                if foundSub1 and foundSub2:
                    return True
                
            return False
        

        # walk through and create a dict of the chars in each string.
        # check if the dicts are equal
        dict1 = {}
        dict2 = {}

        if s1 in self.masterScrambles:
            dict1 = self.masterScrambles[s1]
        else:
            for i in s1:
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1
            self.masterScrambles[s1] = dict1
        
        if s2 in self.masterScrambles:
            dict2 = self.masterScrambles[s2]
        else:
            for i in s2:
                if i in dict2:
                    dict2[i] += 1
                else:
                    dict2[i] = 1
            self.masterScrambles[s2] = dict2
        
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

        return scramble(self, s1, "", "")


        
# @lc code=end


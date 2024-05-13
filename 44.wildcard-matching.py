# @before-stub-for-debug-begin
from python3problem44 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def  checkSubStringRight(self, s:str, groups:list, removedLeft:int) -> bool:
        # we can skip any amount of string on the left before the first group
        # so check from the right over
        if len(groups) == 0:
            return True
        
        groupIndex = len(groups)-1
        i = len(s)-1
        while i >= 0:
            # is valid placement
            if i+removedLeft not in positions[groups[groupIndex]] and positions[groups[groupIndex]] != -1:
                return False
            
            groupIndex -= 1
            if groupIndex == 0:
                return True
            if groups[groupIndex] != "*":
                i -= len(groups[groupIndex])
                continue
            
            return self.checkSubStringLeft(s[:i], groups[:groupIndex], removedLeft)


        return False
    
    def checkSubStringLeft(self, s:str, groups:list, removedLeft:int) -> bool:
        # we can skip any amount of string on the right before the first group
        # so check from left over
        if len(groups) == 0:
            return True
        groupIndex = 0
        i = 0
        while i < len(s):
            # is valid placement
            if i+removedLeft not in positions[groups[groupIndex]] and positions[groups[groupIndex]] != -1:
                return False
            
            groupIndex += 1
            if groupIndex == len(groups):
                return True
            
            if groups[groupIndex] != "*":
                i += len(groups[groupIndex])
                continue
            
            return self.checkSubStringRight(s[i:], groups[groupIndex:], i+removedLeft)


        return False
    
    def isMatch(self, s: str, p: str) -> bool:
        # break match pattern into groups
        # either ? * or groups of chars
        # for regular chars find all the possible match locations in the string
        # check if we theres a spot where a groups start location + its length
        # corresponds to the next group

        # ? can start at every pos and l or 1
        # * can start at every pos and l is any

        # if we ever can complete the string with no remaining groups we win
        # since we're searching left to right if we hit the end the string and
        # have groups left over we cant squeeze them in. return false

        groups = []
        subgroup = ""
        for i in p:
            if i == "?" or i == "*":
                if subgroup != "":
                    groups.append(subgroup)
                subgroup = ""
                groups.append(i)
                continue
            subgroup += i

        if subgroup != "":
            groups.append(subgroup)
            
        positions = {}

        for g in groups:
            if g == "?" or g == "*":
                # -1 is any
                positions[g] = {-1}
            for i, v in enumerate(s):
                if s[i:len(g)+i] == g:
                    if g in positions:
                        (positions[g]).add(i)
                        continue
                    positions[g] = {i}

        groupIndex = 0
        i = 0
        while i < len(s):
            # is valid placement
            g = groups[groupIndex]
            if i not in positions[g] and -1 not in positions[g]:
                return False
            
            groupIndex += 1
            # if we finished the groups check if we matched the whole string
            if groupIndex == len(groups):
                return i == len(s)
            
            # valid placement
            if groups[groupIndex] != "*":
                i += len(groups[groupIndex])
                continue

            return self.checkSubString(s[i:], groups[groupIndex:], i)
            # idk how to handle wildcard

        return False
            

        
# @lc code=end


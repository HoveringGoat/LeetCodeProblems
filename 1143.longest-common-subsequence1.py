#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # some init setup
        setA = self.getOrderedSet(text1)
        setB = self.getOrderedSet(text2)
        return self.getLongestSubsequenceFromSets(setA, setB)
            
    def getLongestSubsequenceFromSets(self, setA: tuple[List,dict], setB: tuple[List,dict]):
        self.reviseSets(setB, setA)

        # trivial case: matching sets
        if setA[0] == setB[0]:
            return len(setA[0])

        # trivial case
        if len(setA[0]) == 0 or len(setB[0]) == 0:
            return 0        
        
        # first elements match. it is part of the subsequence. pop and re-attempt.
        if setA[0][0] == setB[0][0]:
            self.popNthElement(setA, 0)
            self.popNthElement(setB, 0)
            return 1 + self.getLongestSubsequenceFromSets(setA, setB)
        # last elements match
        if setA[0][-1] == setB[0][-1]:
            self.popNthElement(setA, -1)
            self.popNthElement(setB, -1)
            return 1 + self.getLongestSubsequenceFromSets(setA, setB)
        
        # trivial case of redundant elements. first matches last.
        if setA[0][-1] == setB[0][0]:
            value = setA[0][-1]
            if setA[1][value] == 1 and setB[1][value] > 1:
                # only remove from the edge on B
                self.popNthElement(setB, 0)
                return self.getLongestSubsequenceFromSets(setA, setB)
        
            if setA[1][value] > 1 and setB[1][value] == 1:
                # only remove from edge on A
                self.popNthElement(setA, -1)
                return self.getLongestSubsequenceFromSets(setA, setB)
            
            # remove both in the case they each have 1 element or both more than 1
            self.popNthElement(setA, -1)
            self.popNthElement(setB, 0)
            return self.getLongestSubsequenceFromSets(setA, setB)

        # trivial case of redundant elements. first matches last.
        if setA[0][0] == setB[0][-1]:
            value = setA[0][0]
            if setA[1][value] == 1 and setB[1][value] > 1:
                # only remove from the edge on B
                self.popNthElement(setB, -1)
                return self.getLongestSubsequenceFromSets(setA, setB)
        
            if setA[1][value] > 1 and setB[1][value] == 1:
                # only remove from edge on A
                self.popNthElement(setA, 0)
                return self.getLongestSubsequenceFromSets(setA, setB)
            
            # remove both in the case they each have 1 element or both more than 1
            self.popNthElement(setA, 0)
            self.popNthElement(setB, -1)
            return self.getLongestSubsequenceFromSets(setA, setB)
        
        # get max possible subsequence length if the first char IS part of the subsequence
        possibleSubSequenceLength = self.getMaxPossibleSubSequence(setA, setB, 0)
        
        # remove first element
        value = setA[0].pop(0)
        setA[1][value] -= 1

        # duplicate sets so we have an intact copy if we need to check the other path
        # copied sets when first value is the first in the subsequence
        copyA = self.duplicate(setA)
        copyB = self.duplicate(setB)
        self.popUntil(copyB, value)

        # attempt to continue getting longest subsequence discarding this first value
        # (assumes it is NOT in the subsequence)
        discardedLength = self.getLongestSubsequenceFromSets(setA, setB)

        # check if found subsequence length is greater than the largest possible subsequence with the removed value
        if discardedLength >= possibleSubSequenceLength:
            return discardedLength
        
        # max possible value was larger. Now we check if it actually WAS larger
        actualSubSequenceLength = 1 + self.getLongestSubsequenceFromSets(copyA, copyB)
        return max(actualSubSequenceLength, discardedLength)
    
    def popUntil(self, setA: tuple[List,dict], value):
        values = setA[0].copy()
        for i in values:
            if i == value:
                setA[0].remove(i)
                setA[1][i] -= 1

                return
            setA[0].remove(i)
            setA[1][i] -= 1
        
    def duplicate(self, setA: tuple[List,dict]) -> tuple[List,dict]:
        list = setA[0].copy()
        dict = setA[1].copy()
        return (list, dict)

    def getMaxPossibleSubSequence(self, setA: tuple[List,dict], setB: tuple[List,dict], index: int):
        # note index should only be first or last
        # get how many POSSIBLE values could be in this subsequence
        value = setA[0][index]
        found: bool = False
        count: int = 0
        for i in setB[0]:
            if found:
                count += 1
            if i != value:
                count += 1
                found = True
        return count
        
    def popNthElement(self, setA: tuple[List,dict], index: int):
        value = setA[0].pop(index)
        setA[1][value] -= 1
        
    def reviseSets(self, setA: tuple[List,dict], setB: tuple[List,dict]):
        # update the entries in the sets to make sure they match each other
        remove = []
        for key in setA[1].keys():
            if key not in setB[1].keys() or setB[1][key] <= 0:
                remove.append(key)
        for key in remove:
            count = setA[1].pop(key)
            for i in range(count):
                setA[0].remove(key)
                    
        remove = []
        for key in setB[1].keys():
            if key not in setA[1].keys() or setA[1][key] <= 0:
                remove.append(key)
        for key in remove:
            count = setB[1].pop(key)
            for i in range(count):
                setB[0].remove(key)

    def getOrderedSet(self, string: str) -> tuple[List, dict]:
        list = []
        counts = {}
        for i in string:
            list.append(i)
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        return (list, counts)
# @lc code=end


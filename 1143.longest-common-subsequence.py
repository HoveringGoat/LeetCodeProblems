#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        setsA = []
        setsB = []
        setIndex = 0
        setsA.append(self.getOrderedSet(text1))
        setsB.append(self.getOrderedSet(text2))
        self.reviseSets(setsA, setsB, setIndex)
        self.reviseSets(setsB, setsA, setIndex)
        while True:
            setIndex += 1
            #revise set a
            self.addSet(setsA, setIndex+1)
            self.reviseSets(setsA, setsB, setIndex)
            if len(setsA[setIndex]) == 0:
                return setIndex

            #revise set b
            self.addSet(setsB, setIndex+1)
            self.reviseSets(setsB, setsA, setIndex)
            if len(setsB[setIndex]) == 0:
                return setIndex

            # terminal cases
            if setsA[setIndex] == setsB[setIndex]:
                # trivial case find largest substring of set
                return self.getLargestSubsequence(setsA, setIndex)
            
        
    def reviseSets(self, setsA: List[List], setsB: List[List], setIndex: int):
        # given sets revise index based on the other
        unorderedSet = set(setsB[setIndex])
        newSet = []
        for i in setsA[setIndex]:
            if i in unorderedSet:
                newSet.append(i)
        setsA[setIndex] = newSet

    def addSet(self, sets: List[List], subSequenceLength: int):
        # adds the next set of subsequence strings
        previousSet = set(sets[subSequenceLength-2])

        # generate subsequences
        newSet = self.generateSubSequences(sets[0], subSequenceLength)
        newSet = self.removeMissingSets(newSet, previousSet)
        sets.append(newSet)

    def generateSubSequences(self, baseSet: List, subSequenceLength) -> List[str]:
        # generate a subsequence of the desired length from the base set
        # ensure previous sets are matched
        if len(baseSet) == subSequenceLength:
            return [baseSet.join]
        subSequences = []
        # subsequences that start with the first char in the base set
        subSetSubsequences = self.generateSubSequences(baseSet[1:], subSequenceLength-1)
        for i in subSetSubsequences:
            subSequences.append(f"{baseSet[0]}i")
        
        excluded = self.generateSubSequences(baseSet[1:], subSequenceLength)
        for i in excluded:
            subSequences.append(i)
        return subSequences
            
    def removeMissingSets(self, newSet: List[str], previousSet: set[str]) -> List[str]:
        updateSet = []
        toSet = set(newSet)
        for i in toSet:
            for p in previousSet:
                if p in i:
                    updateSet.append(i)
                    break
        return updateSet

    def getOrderedSet(self, string: str) -> List:
        map = []
        for i in string:
            map.append(i)
        return map

    def getLargestSubsequence(self, sets: List[List], setIndex) -> int:
        if len(sets[setIndex]) == 0:
            return len(sets[setIndex-1][0])

        setIndex += 1
        self.addSet(sets, setIndex+1)
        return self.getLargestSubsequence(sets, setIndex)
# @lc code=end


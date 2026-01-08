#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
from typing import List

# failing: ""mhunuzqrkzsnidwbun"\n"szulspmhwpazoxijwbq""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1, text2 = self.reviseSets(text1, text2)
        # some trivial cases
        if len(text1) == 0 or len(text2) == 0:
            return 0
        if text1[0] == text2[0]:
            print("found common subsequence element - removing first char")
            print(f"Text1: {text1[1:]}")
            print(f"Text2: {text2[1:]}")
            length = 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
            print(f"Maximum subsequence length: {length}")
            return length
        if text1[-1] == text2[-1]:
            print("found common subsequence element - removing last char")
            print(f"Text1: {text1[:-1]}")
            print(f"Text2: {text2[:-1]}")
            length = 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1])
            print(f"Maximum subsequence length: {length}")
            return length
        
        # if we are here we should have significantly reduced strings to work with.
        # perform a double loop and get all the hits for chars in text1 in text 2
        print("Found minimal text sets:")
        print(f"Text1: {text1}")
        print(f"Text2: {text2}")

        # hits is an array of tuples with the format (index of hit in text1, index of hit in text2)
        hits = []
        for index_i, i in enumerate(text1):
            for index_j, j in enumerate(text2):
                if i == j:
                    hits.append((index_i,index_j))
        
        # now we check the hits and create a list of possible subsequences by counting increasing values of j
        # eg (1, 1) -> (2, 4) -> (3, 5)
        # this represents a subsequence where we hit the first second, and third values in text1. or first, fourth and fifth in text 2

        maxLength = 0
        subsequences = self.getAllSubSequences(hits)
        print(f"Subsequences: {subsequences}")
        for s in subsequences:
            maxLength = max(maxLength, len(s))

        print(f"Maximum subsequence length: {maxLength}")
        return maxLength

    def getAllSubSequences(self, hits: tuple[int,int]) -> List[List[int]]:
        subsequences = []
        subsequence = []
        usedIndicies = set()
        print(f"GetSubsequences from: {hits}")

        # for brevity i is the value in hit corresponding to the index of the value in text1
        # j is the value in hit corresponding to the index of the value in text2
        isGettingOtherSubSequences = False
        for index, (i, j) in enumerate(hits):
            if subsequence == [] or (j > subsequence[-1] and i not in usedIndicies):
                subsequence.append(j)
                usedIndicies.add(i)
            else:
                # only do the first time. Since this will get any further subsequences we dont need to check again
                if not isGettingOtherSubSequences:
                    # get all other subsequences in this subsection and add them to our overall list
                    isGettingOtherSubSequences = True
                    otherSubsequences = self.getAllSubSequences(hits[index:])
                    for otherSubsequence in otherSubsequences:
                        subsequences.append(otherSubsequence)

        # ensure we add only non empty subsequences
        if len(subsequence) > 0:
            subsequences.append(subsequence)
        return subsequences

    def reviseSets(self, left: str, right: str):
        # update the elements in the strings to make sure they have matching sets
        left_set: set = set(left)
        right_set: set = set(right)

        if left_set == right_set:
            return (left, right)

        updatedA = ""
        for i in left:
            if i in right_set:
                updatedA += i

        updatedB = ""
        for i in right:
            if i in left_set:
                updatedB += i

        print("revising sets...")
        print(f"text1: {left} -> {updatedA}")
        print(f"text2: {right} -> {updatedB}")
        return (updatedA, updatedB)

        
# @lc code=end


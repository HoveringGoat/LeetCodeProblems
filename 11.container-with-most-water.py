# @before-stub-for-debug-begin
from python3problem11 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # some thoughts: to avoid brute forcing we need a way to quickly "skip"
        # bad heights. If we could quickly check the biggest possible container
        # with a dealy we could spit out its theoretical max - without looking 
        # at all the neighbors. Store max size and look up against that and furthest
        # away. (this wont be the actual max but if its less we can skip)

        heightSorted = sorted(height)
        start = 0
        n = len(height)
        isSorted = (heightSorted == height)
        maxArea = self.assumedMax(height, n)

        for i in range(n):
            currentMax = self.getCurrentMax(height[i], i, n-1)
            if currentMax < maxArea:
                continue
            if isSorted:
                maxArea = currentMax
                continue

            # if (i+1<n):
            #     nextMax = self.getCurrentMax(height[i+1], i+1, maxIndex)
            #     if nextMax > currentMax:
            #         continue
            # dont need to check values already checked
            skips = 0
            for j in range(1, n-i):
                if (j+i < n-1):
                    # check if next value is better - sk
                    # ip if it is
                    if (height[j+i+1]>height[j+i]):
                        skips += 1
                        if skips * height[j+i-skips+1] > maxArea:
                            maxArea = skips * height[j+i-skips+1]
                            if self.getCurrentMax(height[i], i, n) < maxArea:
                                i += 1
                                break
                        continue

                #okay do the checking
                # j is the distance
                skips = 0
                h = height[i]
                if h > height[j+i]:
                    h = height[j+i]
                containerArea = h*j
                if containerArea > maxArea:
                    maxArea = containerArea
        return maxArea
    
    def assumedMax(self, height:List[int], n:int):
        h = height[n-1]
        i = int((n-1)*.7)
        l = (n-1) - i
        t = height[i]
        if h>t:
            return l * t
        return l * h
    
    def getCurrentMax(self, height: int, i:int, maxIndex:int) -> int:
        length = maxIndex-i
        return length * height
        
        
# @lc code=end


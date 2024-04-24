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
        # try to narrow down the possible left and right "walls"
        leftIndex = 0
        rightIndex = len(height)-1
        foundLeft = False
        foundRight = False
        currentMax = rightIndex
        if height[leftIndex] < height[rightIndex]:
            currentMax *= height[leftIndex]
        else:
            currentMax *= height[rightIndex]

        while (not foundLeft or not foundRight) and leftIndex<rightIndex:
            # try moving left end rightward
            if height[leftIndex] < height[rightIndex] and not foundLeft:
                # left side is smaller than right we can possibly improve!
                foundLeft = True
                for i in range(leftIndex+1, rightIndex, 1):
                    if height[i] > height[leftIndex]:
                        # check area
                        currentArea = rightIndex - i
                        if height[i] < height[rightIndex]:
                            currentArea *= height[i]
                        else:
                            currentArea *= height[rightIndex]
                        if currentArea > currentMax:
                            currentMax = currentArea

                        leftIndex = i
                        foundLeft = False
                        # reset the found bool so we will continue searching later
                        break
                # if the found bool WASNT reset then we checked all the values and this is best 

            # else try moving right wall leftwards
            elif height[rightIndex] < height[leftIndex] and not foundRight:
                foundRight = True
                for i in range(rightIndex-1, leftIndex, -1):
                    if height[i] > height[rightIndex]:
                        # check area
                        currentArea = i - leftIndex
                        if height[i] < height[leftIndex]:
                            currentArea *= height[i]
                        else:
                            currentArea *= height[leftIndex]
                        if currentArea > currentMax:
                            currentMax = currentArea
                            
                        rightIndex = i
                        foundRight = False
                        # reset the found bool so we will continue searching later
                        break
            else:
                # we're stuck. try incrementing if we're not done
                if not foundLeft:
                    leftIndex += 1
                if not foundRight:
                    rightIndex -= 1
                    
                # calc new area
                currentArea = rightIndex - leftIndex
                if height[leftIndex] < height[rightIndex]:
                    currentArea *= height[leftIndex]
                else:
                    currentArea *= height[rightIndex]
                if currentArea > currentMax:
                    currentMax = currentArea

        return currentMax
        
# @lc code=end


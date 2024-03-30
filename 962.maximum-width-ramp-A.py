#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        # keep track of each passed number.
        # If we hit a number that is higher than it record how big the width is
        # maybe keep track of active indicies?
        # if new index is higher than any of our current values (aka we update any map values)
        # we can safely ignore that one. It would be a subset of the largest width
        # but keep updating the map value if its >
        
        activeIndexes = []
        currentIndex = 0
        currentMax = 0
    
        for value in nums:
            hasUpdatedMap = False
            for i in range (len(activeIndexes)-1, -1 , -1):
                if value >= nums[activeIndexes[i]]:
                    hasUpdatedMap = True
                    t = currentIndex - activeIndexes[i] # calcWidth
                    if t > currentMax:
                        currentMax = t
                else:
                    break
            if not hasUpdatedMap:
                # we didnt update anything. Must be a new low value
                # ensure it could possibly be a larger ramp than whatever we've found so far
                if currentIndex+currentMax<len(nums):
                    activeIndexes.append(currentIndex)
            currentIndex += 1
        return currentMax
# @lc code=end


#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        lastValue = 0
        lastValueIndex = 0
        lastValueWater = 0
        water = 0
        for index, value in enumerate(height):
            waterTrapped = lastValue - value
            if waterTrapped <= 0:
                lastValue = value
                lastValueIndex = index
                lastValueWater = water
            else:
                water += waterTrapped
        
        # discard everything after the last "max" height
        # reverse array and count water from the other side
        water = lastValueWater
        lastValue = 0

        # would be nice if enumerate had a "reverse" option.
        # I could reverse the array too but then the index would be diff
        for index in range(len(height)-1, lastValueIndex, -1):
            waterTrapped = lastValue - height[index]
            if waterTrapped <= 0:
                lastValue = height[index]
            else:
                water += waterTrapped

        return water
        
# @lc code=end


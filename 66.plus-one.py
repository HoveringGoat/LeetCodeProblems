#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = 1
        while True:
            digits[-1*index] += 1
            if digits[-1*index] != 10:
                return digits
            
            digits[-1*index] -= 10
            if index == len(digits):
                return [1] + digits
            index += 1

        
# @lc code=end


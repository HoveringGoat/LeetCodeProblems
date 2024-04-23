#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zerosFound = 0
        for i in nums:
            if i == 0:
                zerosFound +=1
                continue
            totalProduct *= i

        if zerosFound > 1:
            totalProduct = 0

        answers = []
        for i in nums:
            if zerosFound > 0:
                if i == 0:
                    answers.append(totalProduct)
                else:
                    answers.append(0)
                continue
                
            answers.append(int(totalProduct/i))
        return answers
        
# @lc code=end


#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        hasMost = []
        for i in candies:
            hasMost.append(i+extraCandies >= maxCandies)
        return hasMost


        
# @lc code=end


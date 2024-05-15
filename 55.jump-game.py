#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # walking back from the end of the array we need to find values that are greater than or equal
        # to the distance to the end.
        # if we find any check if they canJump as well
        if len(nums) < 2:
            return True
        jumpable = {0}
        used = set()
        while len(jumpable) > 0:
            nextJumps = set()
            for i in jumpable:
                if nums[i] < 1:
                    continue
                for j in range(i+1, nums[i]+1+i):
                    if j not in used:
                        if j >= len(nums) - 1:
                            return True
                        nextJumps.add(j)
                        used.add(j)
            jumpable = nextJumps 
        
        return False
            
        
# @lc code=end


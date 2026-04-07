#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return self.getSubSets(k, n, nums)
        
    def getSubSets(self, k: int, n: int, nums: List[int]) -> List[List[int]]:
        # null case
        if n <= 0 or k <= 0 or k > n:
            return []
        
        if k == 1:
            if n in nums:
                return [[n]]
            return []
        
        valid_sets = []

        # reduce nums
        while len(nums) > 0 and nums[-1] > n:
            nums = nums[:-1]
        if len(nums) == 0:
            return []
        
        # assume nums[0] is in set
        subsets_a = self.getSubSets(k-1, n-nums[0], nums[1:])
        for i in subsets_a:
            temp = nums[:1]
            temp.extend(i)
            valid_sets.append(temp)
        
        # assume nums[0] is NOT in set
        subsets_b = self.getSubSets(k, n, nums[1:])
        valid_sets.extend(subsets_b)

        return valid_sets

            
# @lc code=end


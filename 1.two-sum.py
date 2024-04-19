#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        orderedNums = {}
        for i in range(len(nums)):
            if nums[i] in orderedNums:
                if nums[i] * 2 == target:
                    return [orderedNums[nums[i]], i]
            orderedNums[nums[i]] = i

        nums.sort()

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                # rest are too big skip
                a = nums[i] + nums[j]
                if a > target:
                    break
                elif a == target:
                    return [orderedNums[nums[i]], orderedNums[nums[j]]]

        # shouldnt hit if there is a solution
        return []
        
# @lc code=end


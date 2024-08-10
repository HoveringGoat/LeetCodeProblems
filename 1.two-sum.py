#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}
        for (index, value) in enumerate(nums):
            # calculate the match needed to hit the target 
            diff = target - value

            # check if the match is in the map
            if diff in map:
                return [map[diff], index]
            
            # no match in map. Add value so match can find this value
            map[value] = index

        return [0,0]
    
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


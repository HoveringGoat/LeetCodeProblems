#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = 0
        index2 = 0
        if len(nums2) == 0:
            return
        while index1 < len(nums1):
            if index1 < len(nums1) - len(nums2):
                if nums1[index1] <= nums2[index2]:
                    index1 += 1
                else:
                    #swap
                    t = nums1[index1]
                    nums1[index1] = nums2[index2]
                    nums2[index2] = t
                    nums2.sort()
                    index1 += 1
            else:
                nums1[index1] = nums2[index2]
                index1 += 1
                index2 += 1

# @lc code=end


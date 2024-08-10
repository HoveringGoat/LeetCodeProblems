#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # init heap to first k elements of list
        heap = nums[:k]
        heapq.heapify(heap)
        l = len(nums)
        i = k

        # look through the rest of the values
        # replacing values if the new one is greater than the current kth smallest value

        while i < l:
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
            i += 1
        return heapq.heappop(heap)

        
# @lc code=end


#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # convert to dict

        # walk through  keys in dict try and find the value n to make k.
        # -1 from its value in the dict and own
        # proceed to end.
        # return counter for the pairs found

        pairs = 0
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
                continue
            d[i] = 1

        for i in d.keys():
            n = k - i
            if n in d:
                while d[n] > 0 and d[i] > 0:
                    if n == i and d[n] < 2:
                        break
                    pairs += 1
                    d[n] -= 1
                    d[i] -= 1

        return pairs
        
# @lc code=end


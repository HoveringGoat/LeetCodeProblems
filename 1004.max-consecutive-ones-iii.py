# @before-stub-for-debug-begin
from python3problem1004 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # two pointers. one at "head" one at the "tail"
        # keep track of len of substring and used k's
        # if we need to flip a zero and no k's available 
        # we have to go to the tail and free up the first zero
        # and any preceding ones

        head = 0
        tail = 0
        availableK = k
        zeroCounter = 0
        zeroIndexTracker = []
        max = min(len(nums), k)
        for i,v in enumerate(nums):
            if v == 0:
                zeroIndexTracker.append(i)
                if availableK > 0:
                    # use a k dont move tail
                    availableK -= 1
                    if i+1 - tail > max:
                        max = i+1 - tail
                    continue
                # no k's free move tail up
                tail = zeroIndexTracker[zeroCounter]+1
                zeroCounter += 1
                continue
            # found a 1 yay!
            if i+1 - tail > max:
                max = i+1 - tail

        return max



        # combine 1's to be the number of 1's in that sequence
        # [1,1,1,0,0,0,1,1,1,1,0] -> [3,0,0,0,4,0]
        # we can quickly check if any sequences can be merged 
        # and keep track of maximum

        c = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                continue
            if count > 0:
                c.append(count)
                count = 0
            c.append(0)
        
        if count > 0:
            c.append(count)

        max = min(len(nums), k)
        for i,v in enumerate(c):
            if v == 0:
                continue
            cur = v
            availableK = k
            for j in range(i+1, len(c)+1):
                # handle end edge case
                if j == len(c):
                    cur += availableK
                    cur = min(len(nums), cur)
                    if cur > max:
                        max = cur
                    break

                if c[j] == 0:
                    if availableK > 0:
                        # if its a zero try and flip it and continue
                        cur += 1
                        availableK -= 1
                        continue
                    # we're out of k's
                    if cur > max:
                        max = cur
                    break
                cur += c[j]
        
        return max


        
# @lc code=end


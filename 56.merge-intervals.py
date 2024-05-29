# @before-stub-for-debug-begin
from python3problem56 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by the first range asc
        # we can then check if the next range is within the current one
        # if it is expand, else add the old range to the return list and move on

        mergedIntervals = []
        intervals.sort()
        currentInterval = intervals[0]
        for i in intervals[1:]:
            # check if interval is within range
            if i[0] <= currentInterval[1]:
                currentInterval[1] = max(currentInterval[1], i[1])
                continue
            # not in range
            mergedIntervals.append(currentInterval)
            currentInterval = i

        mergedIntervals.append(currentInterval)
        return mergedIntervals


# @lc code=end


# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # we're going to iterate through going from reading the top row left to right
        # right col top to bot bottom row right to left and left col bot to top
        # each time we complete a row or col we remove that row/col from our search
        # we'll keep track of our bound with a minI maxI and minj maxJ.
        # in the while loop we will keep track of what we're currently iterating over

        minI = 0
        maxI = len(matrix)-1
        minJ = 0
        maxJ = len(matrix[0])-1

        cur = "top"
        i = 0
        j = 0
        spiralArray = []
        while minJ <= maxJ and minI <= maxI:
            if cur == "top":
                # iterate on top row from left to right
                # increase j from minJ -> maxJ
                if j > maxJ:
                    cur = "right"
                    minI += 1
                    i = minI
                    j = maxJ
                    continue
                spiralArray.append(matrix[i][j])
                j += 1
                continue
            elif cur == "right":
                # iterate on right col from top to bot
                # increase i from minI -> maxI
                if i > maxI:
                    cur = "bot"
                    maxJ -= 1
                    j = maxJ
                    i = maxI
                    continue
                spiralArray.append(matrix[i][j])
                i += 1
                continue
            elif cur == "bot":
                # iterate on bottom row from right to left
                # decrease j from maxJ -> minJ
                if j < minJ :
                    cur = "left"
                    maxI -= 1
                    j = minJ
                    i = maxI
                    continue
                spiralArray.append(matrix[i][j])
                j -= 1
                continue
            elif cur == "left":
                # iterate on right col from top to bot
                # increase i from minI -> maxI
                if i < minI:
                    cur = "top"
                    minJ += 1
                    j = minJ
                    i = minI
                    continue
                spiralArray.append(matrix[i][j])
                i -= 1
                continue

        return spiralArray
        
# @lc code=end


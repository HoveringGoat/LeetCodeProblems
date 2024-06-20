# @before-stub-for-debug-begin
from python3problem69 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search the sqrt
        min = 0
        max = x
        while min < max:
            guess = int((min+max) * .5)
            squared = guess * guess
            if squared > x:
                max = guess - 1
                continue
            else:
                if squared + guess + guess >= x:
                    return guess
                min = guess + 1
            
        return min
        
# @lc code=end


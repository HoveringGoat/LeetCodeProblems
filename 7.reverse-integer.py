#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        negative = x<0

        stringX = str(x)

        if negative:
            stringX = stringX[1:]
        
        s = stringX[::-1]

        reversed = int(s)

        if negative:
            reversed *= -1

        if reversed > 2147483647 or reversed < -2147483648:
            return 0
        return reversed
        
# @lc code=end


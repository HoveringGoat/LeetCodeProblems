#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringInt = str(x)
        for i in range(int(len(stringInt)/2)):
            if stringInt[i] != stringInt[-1*(i+1)]:
                return False
        return True
        
# @lc code=end


#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        trimmedString = ""

        for index, char in enumerate(s.strip()):
            ascii = ord(char)
            # is num 0-9
            if ascii >= 48 and ascii <= 57:
                trimmedString+=char
                continue
            if char == "-" and index == 0:
                trimmedString+=char
                continue
            if char == "+" and index == 0:
                continue
            
            # nope. Break and parse string up to here
            break
        
        try:
            i = int(trimmedString)

            if i > 0:
                return min(2147483647, i)
            else:
                return max(-2147483648, i)
        except:
            return 0
        
# @lc code=end


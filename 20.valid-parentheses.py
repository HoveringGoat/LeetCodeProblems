#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        map = {}
        map['('] = ')'
        map['['] = ']'
        map['{'] = '}'
        currentBracket = []
        # get next bracket and then walk to its match.
        for value in s:
            if value in map:
                currentBracket.append(map[value])
            elif len(currentBracket) <= 0 or currentBracket[-1] != value:
                    return False
            else:
                 currentBracket.pop()

        return len(currentBracket) == 0
        
# @lc code=end


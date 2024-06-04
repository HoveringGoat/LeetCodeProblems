#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
class Solution:
    def getMapOfWord(self, word):
        map = {}
        for i in word:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        return map
    
    def closeStrings(self, word1: str, word2: str) -> bool:
        # order doesnt matter because we can transpose chars as needed
        # first are the strings the same length - we cannot add or remove chars
        # are all the chars present - we cant magic up char
        # are all the chars in the correct quanity. we CAN shift around the amounts
        # if there are 1 a 2 b and 3 c's we can make any letter have any of those amounts
        # but not less or more

        if len(word1) != len(word2):
            return False
        
        map = self.getMapOfWord(word1)
        map2 = self.getMapOfWord(word2)
        
        # ensure keys are same
        if set(map.keys()) != set(map2.keys()):
            return False
            
        return sorted(map.values()) == sorted(map2.values())

# @lc code=end


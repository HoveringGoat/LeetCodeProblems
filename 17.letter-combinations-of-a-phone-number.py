#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7": ["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        lastSet = set()
        
        for i in digits:
            if len(lastSet) == 0:
                for v in mapping[i]:
                    lastSet.add(v)
                continue
            newSet = set()
            for s in lastSet:
                for v in mapping[i]:
                    newSet.add(s+v)
            lastSet = newSet
        return lastSet
        


        
# @lc code=end


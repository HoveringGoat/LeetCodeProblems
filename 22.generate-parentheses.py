#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # two options close current parentheses or open a new one
        allParen = set()

        # first and last are always an opener and a close. The rest are all the combos
        # n =1 01
        # n=2  01,10 -> 0011, 0101
        # n=3  000111, 001011, 011001, 010101
        # 1 = open, -1 = close
        iter = 1
        allParen.add("()")
        while iter < n:
            newSet = set()
            for i in allParen:

                s = "("
                count = 1
                skip = False
                isInvalid = False
                for c in i:
                    if c == ")":
                        count +=1
                        s += "("
                    else:
                        # only disallow "invalid" groups on the last iteration
                        if count == 0:
                            skip = True
                            break
                        count -=1
                        s += ")"
                s+=")"

                # add check to make sure we dont add invalid groups
                if not skip:
                    newSet.add(s)

                s = "("
                s+=i
                s+=")"
                newSet.add(s)
                s = "()"
                s+=i
                newSet.add(s)
                s=i
                s += "()"
                newSet.add(s)

                # add the (())/(()) group
                if (iter +1) % 2 == 0:
                    size = int((iter+1) *.5)
                    s = "(" * size
                    s += ")" * size
                    s += s 
                    newSet.add(s)
                    
            allParen = newSet
            iter += 1
        
        return allParen

        
# @lc code=end


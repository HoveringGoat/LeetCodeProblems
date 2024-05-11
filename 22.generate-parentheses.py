# @before-stub-for-debug-begin
from python3problem22 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # two options close current parentheses or open a new one
        allParen = {}

        iter = 0
        allParen[""] = 1
        while iter < n:
            newSet = {}
            for i in allParen:

                isValid = allParen[i]
                s = "(" + i + ")"
                if s == "(((())))(())":
                    print("found")
                v = min(1,isValid + 1)
                if v == 1 or s not in newSet:
                    newSet[s] = v

                s = ")" + i + "("
                if s == "(((())))(())":
                    print("found")
                v = isValid - 1
                if v == 1 or s not in newSet:
                    newSet[s] = v

                s = "()" + i
                if s == "(((())))(())":
                    print("found")
                if isValid == 1 or s not in newSet:
                    newSet[s] = isValid

                s = i + "()"
                if s == "(((())))(())":
                    print("found")
                if isValid == 1 or s not in newSet:
                    newSet[s] = isValid

                if iter > 3 and i[-1] == ")":
                    s = i[:-1] + "())"
                    if s == "(((())))(())":
                        print("found")
                    if isValid == 1 or s not in newSet:
                        newSet[s] = isValid

                if iter > 3 and i[0] == "(":
                    s = "(()" + i[1:]
                    if s == "(((())))(())":
                        print("found")
                    if isValid == 1 or s not in newSet:
                        newSet[s] = isValid

            allParen = newSet
            iter += 1
            
        valids = []
        for k,v in allParen.items():
            if k == "(((())))(())":
                print("asdas")
            if v == 1:
                valids.append(k)
        
        valids.sort()
        return valids

        
# @lc code=end


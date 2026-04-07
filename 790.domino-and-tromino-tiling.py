#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
class Solution:
    def numTilings(self, n: int) -> int:
        solved_sets = {}

        def solveSubSet(n: int) -> int:
            # null cases
            if n in solved_sets:
                return solved_sets[n]
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            
            # single vert domino
            numsSets = solveSubSet(n-1)

            #print(f"n={n}, single vert dom sets={numsSets}")


            # stacked horizontal dominos
            temp = solveSubSet(n-2)

            #print(f"n={n}, stacked horz dom sets={temp}")
            numsSets += temp
            # triamoinos:
            triaminoSetSize = 3
            triaminoSets = 0

            while n-triaminoSetSize >= 0:
                offset = (n-triaminoSetSize) % 3
                temp = (solveSubSet(n-triaminoSetSize-offset) * 2)
                #print(f"tri. n={n}, triaminoSetSize={triaminoSetSize}, offset={offset}, sets={temp}")
                triaminoSets += temp
                triaminoSetSize += 1
                offset = (n-triaminoSetSize) % 4
                temp = (solveSubSet(n-triaminoSetSize-offset) * 2)
                #print(f"tri. n={n}, triaminoSetSize={triaminoSetSize}, offset={offset}, sets={temp}")
                triaminoSets += temp
                triaminoSetSize += 1

            #print(f"n={n}, triamino sets={triaminoSets}")
            numsSets += triaminoSets

            #print(f"solved set: n={n}, totalsets: {numsSets}")
            solved_sets[n] = numsSets
            return numsSets
        return solveSubSet(n)
        
# @lc code=end


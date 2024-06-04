#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # list of rows list of cols
        # find first element in each list check if equal
        # until we check all elements OR find theyre not equal
        count = 0
        map = {}
        rowCount = 0
        for row in grid:
            r = tuple(row)
            if r in map:
                map[r].append(rowCount)
            else:
                map[r] = [rowCount]
            rowCount += 1
        
        for rowIndex in range(len(grid)):
            col = []
            for colIndex in range(len(grid)):
                col.append(grid[colIndex][rowIndex])
            c = tuple(col)

            if c in map:
                count += len(map[c])
            
        return count

        
# @lc code=end


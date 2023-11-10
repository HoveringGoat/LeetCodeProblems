# @before-stub-for-debug-begin
from python3problem36 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    # check all three "subsections" for no repeating chars (idk if this is sufficient)
    # rows are numbered 0-8 top to bottom
    # cols are numbered 0-8 left to right
    # boxes are numbered 0-8 from top left to bottom right (top right is 2)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if self.isValidSubSection(self.getRow(board, i)) == False:
                return False
        for i in range(9):
            if self.isValidSubSection(self.getColumn(board, i)) == False:
                return False
        for i in range(9):
            if self.isValidSubSection(self.getBox(board, i)) == False:
                return False
        return True
    
    
    def isValidSubSection(self, subsection: List[str]) -> bool:
        tempDict = {}
        for i in subsection:
            if i == ".":
                continue
            if i in tempDict:
                return False
            tempDict[i] = True
        return True
    
    def getColumn(self, board: List[List[str]], col: int) -> List[str]:
        column = []
        for row in board:
            column.append(row[col])
        return column
    
    def getRow(self, board: List[List[str]], row: int) -> List[str]:
        return board[row]

    def getBox(self, board: List[List[str]], boxNum: int) -> List[str]:
        #modBox = boxNum % 3
        #divBox = int(boxNum / 3)

        # if mod == 0 then we are left boxes
        # if mod == 1 then middle
        # if mod == 2 then right
        
        # if div == 0 then we are top rows
        # if div == 1 then middle rows
        # if div == 2 then bottom rows

        # will be 0,3,6
        startingRow = int(boxNum / 3) * 3
        startingCol = (boxNum % 3) * 3
        box = []
        for i in range(startingRow,startingRow+3):
            for j in range(startingCol,startingCol+3):
                box.append(board[i][j])
        return box
    

# @lc code=end


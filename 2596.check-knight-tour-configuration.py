#
# @lc app=leetcode id=2596 lang=python3
#
# [2596] Check Knight Tour Configuration
#

# @lc code=start
from typing import List

class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        i = 0
        lastX = 0
        lastY = 0
        n = len(grid)
        gridsize = n*n
        
        # theres a little detail that says it has to start top left. smdh 
        if grid[0][0] != 0:
            return False
        
        i += 1
        while i < gridsize:
            # setup bounds to search for the next value
            minx = 0
            maxx = n
            miny = 0
            maxy = n
            if (lastX-2 > minx):
                minx = lastX-2
            if (lastX + 3 < maxx):
                maxx = lastX+3
            if (lastY-2 > miny):
                miny = lastY-2
            if (lastY + 3 < maxy):
                maxy = lastY+3

            found = False
            for x in range(minx, maxx):
                if found:
                    break
                for y in range(miny, maxy):
                    if grid[y][x] == i:
                        #check if its within expected bounds
                        xdiff = abs(lastX - x)
                        ydiff = abs(lastY - y)

                        if xdiff+ydiff == 3 and xdiff != 0 and ydiff != 0:
                            #valid
                            lastX = x
                            lastY = y
                            found = True
                            break
                        # not valid return
                        return False
            # not found in the range return
            if not found:
                return False
            i += 1
        return True


if __name__ == "__main__":
    print("Hello, World!")
    grid = [[24,11,22,17,4],[21,16,5,12,9],[6,23,10,3,18],[15,20,1,8,13],[0,7,14,19,2]]
    Solution.checkValidGrid(None, grid)

        
# @lc code=end


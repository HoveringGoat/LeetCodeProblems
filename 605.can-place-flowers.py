#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowers = 0
        index = 0
        last = 0
        while flowers < n and index < len(flowerbed):
            if last == 0:
                if flowerbed[index] == 0:
                    if index+1 == len(flowerbed) or flowerbed[index+1] == 0:
                        flowers += 1
                        index +=2
                        continue
                    
            last = flowerbed[index]
            index += 1

            
        return flowers >= n
        
# @lc code=end


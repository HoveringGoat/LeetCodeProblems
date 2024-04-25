#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuyDay = 0
        bestSellDay = 0
        bestProfit = 0
        currentLowestPrice = None
        currentLowestDay = 0

        for index, value in enumerate(prices):
            if currentLowestPrice is None or value < currentLowestPrice:
                currentLowestPrice = value
                currentLowestDay = index
                continue
            elif value > currentLowestPrice:
                # calc profit
                profit = value - currentLowestPrice
                if profit > bestProfit:
                    # new record
                    bestBuyDay = currentLowestDay
                    bestSellDay = index
                    bestProfit = profit
        
        return bestProfit
# @lc code=end


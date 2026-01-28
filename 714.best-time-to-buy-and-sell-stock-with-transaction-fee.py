#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        currentBuy = 0
        currentSell = 0

        # rules if our current price drops under currentSell - fee then we should take profit and re-buy
        # otherwise we should be looking for a better sell price

        for i, price in enumerate(prices):
            #print(f"index: {i}, price: {price}, currentBuy: {currentBuy}, currentSell: {currentSell}")
            # new buy opp
            if price + fee < prices[currentSell]:
                tradeProfit = prices[currentSell] - prices[currentBuy] - fee
                #print("New buying opportunity. potential trade profit: {tradeProfit}")
                if tradeProfit > 0:
                    profit += tradeProfit
                    #print("Take profit opportunity. Trade profit: {tradeProfit}, totalProfit: {profit}")
                currentBuy = i
                currentSell = i
                continue

            # if price is strictly lower than current buy AND we don't have any potential profit move buy
            if price < prices[currentBuy]:
                tradeProfit = prices[currentSell] - prices[currentBuy] - fee
                if tradeProfit <= 0:
                    #print("New buying opportunity. Move buy without any trade")
                    currentBuy = i
                    currentSell = i
                    continue

            # new sell opp
            if price > prices[currentSell]:
                #print("New sell opportunity")
                currentSell = i
        
        # loop complete 
        # take profit if possible
        if currentBuy != currentSell:
            tradeProfit = prices[currentSell] - prices[currentBuy] - fee
            if tradeProfit > 0:
                #print("Take profit opportunity. Trade profit: {tradeProfit}, totalProfit: {profit}")
                profit += tradeProfit

        return profit
        

        
# @lc code=end


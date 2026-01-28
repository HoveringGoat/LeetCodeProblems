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
        

    # gpts dp method. calculate max profit from each state we could be in each day
    # we own the stock or we dont own the stock
    def maxProfit2(self, prices: List[int], fee: int) -> int:
        # calculate the init values

        # we did not buy stock. cash/profit unchanged
        cash = 0
        # We bought the stock at the first days price. cash is negative at price of stock minus fee
        hold = -prices[0] - fee

        # continue calculating states AFTER the first day
        for p in prices[1:]:
            # what if we didn't own the stock 
            # two possibilities either we already didnt own in which case we carry over our cash balance from yesterday
            # or we are selling.
            nextCash = max(cash, hold + p)

            # what if we did own the stock
            # first option we already own it in which case we continue holding
            # second we sell and take profit
            nextHold = max(hold, cash - p - fee)

            # i originally thought this would cause branching and we couldn't preserve state but optimal trade WILL
            # be preserved in the hold/cash values 
            cash = nextCash
            hold = nextHold

        return cash
# @lc code=end


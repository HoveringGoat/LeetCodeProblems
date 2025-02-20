# @before-stub-for-debug-begin
from python3problem322 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # get max of each coin
        coins.sort()
        maxAmounts = []
        for i in coins:
            max: int = int(amount / i)
            for j in coins[i:]:
                if j % i == 0:
                    t: int = int(j/i - i)
                    if t < max:
                        max = t
                    break
            maxAmounts.append(max)
            
        return self.search(coins, amount, maxAmounts, 0)
        
        
        # brute force search
    def search(self, coins: List[int], amount: int, maxAmounts: List[int], usedCoins: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return usedCoins
        
        for index in range(len(coins)-1, -1, -1):
            max = maxAmounts[index]
            coin = coins[index]
            if amount - coin < 0:
                continue
            t = int(amount/coin)
            if t < max:
                max = t
            for number in range(max, -1, -1):
                value = self.search(coins[:index], amount - coin*number, maxAmounts[:index], usedCoins+number)
                if value != -1:
                    return value
        return -1            
# @lc code=end


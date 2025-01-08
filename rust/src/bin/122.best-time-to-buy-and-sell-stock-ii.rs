/*
 * @lc app=leetcode id=122 lang=rust
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut profit: i32 = 0;
        let mut bought_price: i32 = 0;
        let mut bought: bool = false;
        let mut last_price = prices[0];

        for price in prices{
            if (last_price < price){
                // price went up
                // make sure we are holding since there is profit now
                // if we already bought it was a better price
                if (!bought){
                    bought = true;
                    bought_price = last_price;
                }
            }
            else if (last_price > price){
                // price go down
                // lock in profit (before dip)
                // remove bought stock
                // if we werent holding we can ignore
                if (bought){
                    profit -= bought_price;
                    profit += last_price;
                    bought = false;
                }
            }
            last_price = price;
        }

        if (bought){
            // we're holding so trade off the last day
            profit -= bought_price;
            profit += last_price;
            bought = false;
        }

        return profit;
    }
}
// @lc code=end


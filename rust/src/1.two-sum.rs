/*
 * @lc app=leetcode id=1 lang=rust
 *
 * [1] Two Sum
 */

// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        
        for (index, &value) in nums.iter().enumerate() {
            // calculate the value of a pair
            let diff = target - value;

            // check hashmap for value - if it exists return the pair of indicies
            if let Some(pair) = map.get(&diff) {
                return vec![*pair, index as i32]; 
            }
            // no match found so lets add the corresponding pair to the map.
            map.insert(value, index as i32);
        }

        // shouldnt happen.
        return vec![0,0]
    }
}
// @lc code=end


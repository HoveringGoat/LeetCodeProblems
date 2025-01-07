/*
 * @lc app=leetcode id=169 lang=rust
 *
 * [169] Majority Element
 */

// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut rust_map: HashMap<i32, i32> = HashMap::new();
        let threshold = (nums.len() as i32) /2;

        for i in nums {
            *(rust_map.entry(i).or_insert(0)) += 1;
            let v = *rust_map.get(&i).unwrap();
            if (v > threshold) {
                return i;
            }
        }

        let mut max = 0;
        let mut majority_element = 0;

        for k in rust_map.keys() {
            let v = *rust_map.get(k).unwrap();
            if (v > max){
                max = v;
                majority_element = *k;
            }
        }

        return majority_element;
    }
}
// @lc code=end


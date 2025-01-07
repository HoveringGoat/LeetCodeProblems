/*
 * @lc app=leetcode id=1046 lang=rust
 *
 * [1046] Last Stone Weight
 */

// @lc code=start

use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut sorted_stones: Vec<i32> = stones;
        sorted_stones.sort();
        sorted_stones.reverse();
        while (sorted_stones.len() > 1) {
            let remainder: i32 = sorted_stones.remove(0) - sorted_stones.remove(0);
            
            if (remainder > 0){
                sorted_stones.push(remainder);
                sorted_stones.sort();
                sorted_stones.reverse();
            }
        }

        if (sorted_stones.len() == 1) {
            return sorted_stones[0];
        }

        return 0;
    }
    
    pub fn last_stone_weight_heap(stones: Vec<i32>) -> i32 {

        let mut stone_heap: BinaryHeap<i32> = BinaryHeap::from(stones);

        while (stone_heap.len() > 1) {
            let remainder: i32 = stone_heap.pop().unwrap_or(0) - stone_heap.pop().unwrap_or(0);
            if (remainder > 0){
                stone_heap.push(remainder);
            }
        }
            
        return stone_heap.pop().unwrap_or(0);
    }
}
// @lc code=end


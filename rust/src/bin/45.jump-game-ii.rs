/*
 * @lc app=leetcode id=45 lang=rust
 *
 * [45] Jump Game II
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        // perform all jumps at position to find the earliest we can get to
        // any given position. Check map to store earliest time at position.
        // proceed through the array and using the earliest time in the map
        // to calculate next positions.
        // once we hit the final position we can return

        // trivial case
        if (nums.len() == 1){
            return 0;
        }

        let mut jump_map: HashMap<i32, i32> = HashMap::from([(0,0)]);
        let mut furthest: i32 = 0;
        let end_pos = (nums.len() as i32) -1;

        for pos in 0.. (nums.len() as i32){
            if (!jump_map.contains_key(&pos)) {
                // error condition. There is no solve???
                return -1;
            }

            // get best jumps at this position
            let jumps: i32 = jump_map.get(&pos).unwrap() + 1;
            let range: i32 = nums[pos as usize];

            // ensure theres something useful here
            if (range + pos > furthest){
                for jump_size in 1..(range +1) {
                    let target_pos: i32 = pos + jump_size;
                    // make sure this is a new position
                    if (target_pos > furthest){
                        // exit condition
                        if (target_pos == end_pos){
                            return jumps;
                        }
                        
                        if (!jump_map.contains_key(&target_pos)) {
                            jump_map.insert(target_pos, jumps);
                        }
                    }
                }
                furthest = range + pos;
            }

        }

        return -1;
    }
}
// @lc code=end


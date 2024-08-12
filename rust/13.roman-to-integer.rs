/*
 * @lc app=leetcode id=13 lang=rust
 *
 * [13] Roman to Integer
 */

// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        // create map for converting digits to chars
        // break down numbers into groups of symbols
        // if we have 4 of a symbol use the larger symbol with current preceding it IX instead of VIIII
        let mut map: HashMap<i32, char> = HashMap::new();
        map.insert(1000,'M');
        map.insert(500,'D');
        map.insert(100,'C');
        map.insert(50,'L');
        map.insert(10,'X');
        map.insert(5,'V');
        map.insert(1,'V');

        //let mut remainingValue = parse
        
    }
}
// @lc code=end


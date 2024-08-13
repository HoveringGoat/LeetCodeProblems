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
        let mut map: HashMap<char, i32> = HashMap::new();
        map.insert('M', 1000);
        map.insert('D', 500);
        map.insert('C', 100);
        map.insert('L', 50);
        map.insert('X', 10);
        map.insert('V', 5);
        map.insert('I', 1);
        let mut num = 0;
        let mut current_chunk = 0;
        let mut last_numeral = ' ';
        let mut last_chunk = 0;

        for i in s.chars() {
            if i == last_numeral{
                current_chunk += map.get(&i).expect("failed to get value");
                continue
            }
            
            last_numeral = i;

            // found start of new chunk
            if last_chunk > current_chunk{
                // normal operation add last chunk to num
                num += last_chunk
            }
            else{
                // subtraction
                current_chunk -= last_chunk
            }
            
            last_chunk = current_chunk;
            current_chunk = *map.get(&i).expect("failed to get value");
        }

        if last_chunk > current_chunk{
            // normal operation add last chunk to num
            num += last_chunk
        }
        else{
            // subtraction
            current_chunk -= last_chunk
        }

        num + current_chunk
    }
}
// @lc code=end


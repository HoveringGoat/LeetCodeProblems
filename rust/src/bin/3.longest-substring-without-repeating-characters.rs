/*
 * @lc app=leetcode id=3 lang=rust
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        // keep track of current substring.
        // when we encounter a char thats already in the substring remove that char and elements preceding it
        // add new char and continue
        
        let mut start_index = 0;
        let mut end_index = 0;
        let chars = s.as_bytes();

        // keeps track of location of chars in current substring
        let mut map: HashMap<u8, usize> = HashMap::new(); 
        let mut size = 0;
        let mut max_size = 0; 

        for (index, c) in chars.iter().enumerate() {
            end_index += 1;
            if let Some(map_index) = map.get(&c) {
                // char exists update size
                //println!("found: {c}, removing other entries");
                let new_start_index = *map_index;
                for i in start_index..new_start_index {
                    // remove all of these chars
                    let t = &chars[i];
                    //println!("removed: {t}");
                    map.remove(t);
                    size -= 1;
                }
                map.insert(*c, index);
                //println!("replaced: {c}");
                start_index = new_start_index + 1;
            }
            else {
                // char isnt in current substring
                //println!("added: {c}");
                map.insert(*c, index);
                size += 1;
                if size > max_size{
                    max_size = size;
                }
            }

            //println!("substring: {start_index},{end_index}, size: {size}");
        }

        max_size
        
    }
}
// @lc code=end


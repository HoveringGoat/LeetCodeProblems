/*
 * @lc app=leetcode id=76 lang=rust
 *
 * [76] Minimum Window Substring
 */

// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        // split input string into an array of strings containing either a
        // or make an array of "skips" so we know how far to incremenet the pointers
        // char in the expected char string OR the next set of chars up to the next char in the expected string
        // we can then walk through the array moving the forward pointer to our "window"
        // when we add a matched char also add it to a map keeping track
        // of the chars in our "window" matching the expected chars
        // if we hit a point we have all the chars we have a possible solution
        // length of window is the diff between the two pointers
        // if its a min copy the substring and store it as a possible solution
        // at the end return the solution. - we init it to "" so if we never find a solution thats valid


        // this is an array of ints telling how far to skip a pointer on each "jump"

        let mut solution: String = String::from("");
        let mut match_map: HashMap<char, i32> = HashMap::new();

        for i in t.chars() {
            *(match_map.entry(i).or_insert(0)) += 1;
        }

        let chars: Vec<char> = s.chars().collect();
        
        let mut min_length: usize = s.len() + 1;
        // map to keep count of how many of the "good" chars are in the window
        let mut map: HashMap<char, i32> = HashMap::new();
        let mut rear_window_index = 0;
        let mut front_window_index = 0;

        while (rear_window_index < chars.len()) {
            // speed things along until we find some char that matches
            let mut i: char = chars[rear_window_index];
            if (!match_map.contains_key(&i)) {
                rear_window_index += 1;
                front_window_index += 1;
            }
            else {
                break;
            }
        }
        
        while (rear_window_index < chars.len()) {
            //println!("{}",String::from(&s[rear_window_index..front_window_index]));
            let length: usize = front_window_index - rear_window_index;
            if ((length >= t.len()) &&
                subsection_contains(&map, &match_map)) {
                // we have a match
                // record length and if is a possibly solution save
                //println!("match found: {}", length);
                if (length < min_length) {
                    min_length = length;
                    solution = String::from(&s[rear_window_index..front_window_index]);
                }
                
                let mut i: char = chars[rear_window_index];
                *(map.entry(i).or_insert(0)) -= 1;

                rear_window_index += 1;
                if (rear_window_index < chars.len()) {
                    i = chars[rear_window_index];
                    while(!map.contains_key(&i)) {
                        rear_window_index += 1;
                        if (rear_window_index < chars.len()) {
                            i = chars[rear_window_index];
                        }
                        else {
                            break;
                        }
                    }
                }
                continue;
            }
            else if (front_window_index >= chars.len()) {
                break;
            }

            if (front_window_index < chars.len()) {
                let mut i: char = chars[front_window_index];
                
                while(!match_map.contains_key(&i)) {
                    front_window_index += 1;
                    if (front_window_index < chars.len()) {
                        i = chars[front_window_index];
                    }
                    else {
                        break;
                    }
                }
                
                // either we found the next char or we ran out of chars
                if (match_map.contains_key(&i)) {
                    *(map.entry(i).or_insert(0)) += 1;
                }
                front_window_index += 1;
            }
        }

        return solution;
    }
}

pub fn subsection_contains(map: &HashMap<char, i32>, match_map: &HashMap<char, i32>) -> bool {
    for key in match_map.keys() {
        if (!map.contains_key(key)) {
            return false;
        }

        let map_count = *(map.get(key).unwrap());
        let count = *(match_map.get(key).unwrap());
        if ( map_count < count) {
            return false;
        }
    }

    return true;
}
// @lc code=end


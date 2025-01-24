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

        let mut skip_index: Vec<usize> = Vec::new();
        let chars: Vec<char> = s.chars().collect();
        let mut count: usize = 0;

        for i in s.chars() {
            if (match_map.contains_key(&i)){
                if (count > 0){
                    skip_index.push(count);
                    count = 0;
                }
                skip_index.push(1);
            }
            else{
                count += 1;
            }
        }
        
        let mut min_length: usize = s.len() + 1;
        // map to keep count of how many of the "good" chars are in the window
        let mut map: HashMap<char, i32> = HashMap::new();
        let mut rear_window_index = 0;
        let mut rear_skip_index = 0;
        let mut front_window_index = 0;
        let mut front_skip_index = 0;
        
        while (front_window_index <= chars.len() &&
            rear_window_index <= front_window_index &&
            front_skip_index <= skip_index.len() &&
            rear_skip_index < skip_index.len()) {
            //println!("{}",String::from(&s[rear_window_index..front_window_index]));
            if (subsection_contains(&map, &match_map)){
                // we have a match
                // record length and if is a possibly solution save
                let length: usize = front_window_index - rear_window_index;
                if (length < min_length) {
                    min_length = length;
                    solution = String::from(&s[rear_window_index..front_window_index]);
                }
                
                let indicies_to_increase = skip_index[rear_skip_index];
                let i: char = chars[rear_window_index];
                if (indicies_to_increase == 1 && 
                    map.contains_key(&i)){
                    *(map.entry(i).or_insert(0)) -= 1;
                }
                rear_window_index += indicies_to_increase;
                rear_skip_index += 1;

                if (rear_skip_index < skip_index.len()) {
                    let indicies_to_increase = skip_index[rear_skip_index];
                    let i: char = chars[rear_window_index];
                    if (indicies_to_increase > 1 || !map.contains_key(&i)) {
                        //println!("skipping char(s): '{}'", &s[rear_window_index..rear_window_index+indicies_to_increase]);
                        rear_window_index += indicies_to_increase;
                        rear_skip_index += 1;
                    }
                }

                continue;
            }

            if (front_skip_index < skip_index.len()) {
                let indicies_to_increase = skip_index[front_skip_index];
                let i: char = chars[front_window_index];
                if (indicies_to_increase == 1 && 
                    match_map.contains_key(&i)){
                    *(map.entry(i).or_insert(0)) += 1;
                }
                    
                front_window_index += indicies_to_increase;
                front_skip_index += 1;
            }
            else{
                break;
            }
        }

        return solution;
    }
}

pub fn subsection_contains(map: &HashMap<char, i32>, match_map: &HashMap<char, i32>) -> bool {
    for key in match_map.keys(){
        if (!map.contains_key(key)){
            return false;
        }

        let map_count = *(map.get(key).unwrap());
        let count = *(match_map.get(key).unwrap());
        if ( map_count < count){
            return false;
        }
    }

    return true;
}
// @lc code=end


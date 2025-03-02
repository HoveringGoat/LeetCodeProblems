/*
 * @lc app=leetcode id=30 lang=rust
 *
 * [30] Substring with Concatenation of All Words
 */

use std::str::Chars;

// @lc code=start
impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {

        let mut indicies: Vec<i32> = [].to_vec();
        let word_length: usize = words[0].chars().count();
        let substring_length: i32 = (words.len() * word_length) as i32;
        let max_index: i32 = (s.chars().count() + 1) as i32 - substring_length;

        let mut valid_substrings: Vec<&str> = vec![];

        for i in 0..max_index
        {
            let substring: &str = &(s[i as usize..(i+substring_length) as usize]);
            if valid_substrings.contains(&substring){
                indicies.push(i);
            }
            else if Self::check_substring(&substring, &mut words.clone()){
                valid_substrings.push(substring);
                indicies.push(i);
            }
        }

        return indicies;
    }

    pub fn check_substring(substring: &str, words: &mut Vec<String>) -> bool {
        let word_length: usize = words[0].chars().count();
        //println!("substring: {substring}");
        for i in 0..words.len() {

            let word: &str = &(substring[i*word_length..(i+1)*word_length]);
            
            let mut found: bool = false;
            for i in 0..words.len(){
                if words[i] == word {
                    //println!("word: {word} found");
                    words.remove(i);
                    found = true;
                    break;
                }
            }

            if !found {
                //println!("word: {word} not found");
                return false;
            }

        }
        return true;
    }
}
// @lc code=end


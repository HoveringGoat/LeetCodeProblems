/*
 * @lc app=leetcode id=274 lang=rust
 *
 * [274] H-Index
 */

// @lc code=start
impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        
        let mut sorted_citations = citations;
        sorted_citations.sort();
        let mut max_h: i32 = sorted_citations.len() as i32;

        for i in sorted_citations{
            if (i < max_h){
                max_h -= 1;
                continue;
            }

            // the rest should fit
            break;
        }
        
        return max_h;
    }
}
// @lc code=end


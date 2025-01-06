/*
 * @lc app=leetcode id=2580 lang=rust
 *
 * [2580] Count Ways to Group Overlapping Ranges
 */

// @lc code=start
impl Solution {
    pub fn count_ways(mut ranges: Vec<Vec<i32>>) -> i32 {

        let range = ranges.len();

        for index in 1..range {
            for i in 0..index {
                // skip if we've already combined this range
                if (ranges[i].len() == 0) {
                    continue;
                }

                // skip if ranges are either strictly greater or lesser
                if (ranges[i][1] < ranges[index][0]){
                    continue;
                }
                if (ranges[i][0] > ranges[index][1]){
                    continue;
                }

                // intersection - combine ranges and store in current range
                // remove the early occurring range
                // (since we will check the rest of the ranges against the newly updated one)
                if (ranges[i][0] < ranges[index][0]){
                    ranges[index][0] = ranges[i][0];
                }
                if (ranges[i][1] > ranges[index][1]){
                    ranges[index][1] = ranges[i][1];
                }

                ranges[i] = Vec::new();
            }
        }

        // start at -1 to discount the one group of inter
        let mut distinct_groups: i32  = 0; 
        
        //println!("groups: {ranges:?}");
        
        for i in 0..range{
            let r = &ranges[i];
            //println!("group: {r:?}");
            if (r.len() > 0) {
                distinct_groups += 1
            }
        }

        let number_to_mod: i32 = i32::pow(10,9) + 7;
        let mut groupings: i32 = 1;
        for i in 0..distinct_groups{
            groupings = groupings*2 % number_to_mod;
        }
        println!("distinct groups: {distinct_groups:?}");
        println!("groupings: {groupings:?}");
        
        return groupings;
    }
}
// @lc code=end


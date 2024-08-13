/*
 * @lc app=leetcode id=12 lang=rust
 *
 * [12] Integer to Roman
 */

// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let mut map: HashMap<i32, char> = HashMap::new();
        map.insert(1000,'M');
        map.insert(500,'D');
        map.insert(100,'C');
        map.insert(50,'L');
        map.insert(10,'X');
        map.insert(5,'V');
        map.insert(1,'I');
        
        let sizes = [1000, 500, 100, 50, 10, 5, 1]; 
        let mut remaining_value: i32 = num;
        let mut size_index = 0;
        let mut numerals = String::new();

        while remaining_value > 0 {
            let size = sizes[size_index];
            if remaining_value >= size {
                if size == 500 || size == 50 || size == 5 {
                    if remaining_value >= size * 9/5{
                        let c =*map.get(&sizes[size_index+1]).expect("error getting numeral from map");
                        numerals.push(c);
                        let d =*map.get(&sizes[size_index-1]).expect("error getting numeral from map");
                        numerals.push(d); // larger numeral
                        remaining_value -= size* 9/5;
                        size_index += 2;
                        continue
                    }
                }
                
                let i =  remaining_value/ sizes[size_index];
                let chunk_size = i*sizes[size_index];

                let c = *map.get(&size).expect("error getting numeral from map");
                if i == 4 && size_index > 0{
                    // add one of current and one of +1 size to numeral string
                    numerals.push(c);
                    let d =*map.get(&sizes[size_index-1]).expect("error getting numeral from map");
                    numerals.push(d); // larger numeral
                }
                else {
                    for j in 0..i{
                        numerals.push(c);
                    }
                }

                // reduce remaining value by i*size
                remaining_value -= chunk_size;
                size_index += 1;
            }
            else{
                // last one doesnt fit increase and try next
                size_index += 1;
                continue;
            }
        }
        numerals
    }
}
// @lc code=end


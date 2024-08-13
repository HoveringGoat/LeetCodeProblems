/*
 * @lc app=leetcode id=12 lang=rust
 *
 * [12] Integer to Roman
 */

// @lc code=start
impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let mut map: HashMap<i32, char> = HashMap::new();
        map.insert(1000,'M');
        map.insert(500,'D');
        map.insert(100,'C');
        map.insert(50,'L');
        map.insert(10,'X');
        map.insert(5,'V');
        map.insert(1,'V');
        let num = 0;

        for (index, value) in s.iter().enumerate(){
            println!("index: {index}, value: {value}");
        }

        num
    }

    pub fn roman_to_int(s: String) -> String {
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
        
        let sizes = [1000, 500, 100, 50, 10, 5, 1]; 
        let mut remaining_value: i32 = s.parse().expect("invalid input");
        let mut size_index = 0;
        let mut numerals = String::new();

        while remaining_value > 0 {
            let size = sizes[size_index];
            if remaining_value >= size {
                let i =  remaining_value/ sizes[size_index];
                let c = map.get(&size).expect("error getting numeral from map");
                if i == 4 && size_index > 0{
                    // add one of current and one of +1 size to numeral string
                    numerals.push(c);
                    let d = map.get(&sizes[size_index-1]).expect("error getting numeral from map");
                    numerals.push(d); // larger numeral
                }
                else {
                    for j in ..i{
                        numerals.push(c);
                    }
                }
                // reduce remaining value by i*size
                remaining_value -= i*sizes[size_index];
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


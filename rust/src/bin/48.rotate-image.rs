/*
 * @lc app=leetcode id=48 lang=rust
 *
 * [48] Rotate Image
 */

// @lc code=start
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        // we can swap three times to get the "rotated" positions
        // we repeat for each "position"
        let size = matrix.len();
        let max_index = size-1;
        print_matrix(matrix);

        for row in 0..size-1 {
            for col in row..(size+1)/2 {
                let mut temp = matrix[col][row];
                // swap with diagonal
                matrix[col][row] = matrix[max_index-col][max_index-row];
                matrix[max_index-col][max_index-row] = temp;

                // swap right vertical
                temp = matrix[col][max_index-row];
                matrix[col][max_index-row] = matrix[max_index-col][max_index-row];
                matrix[max_index-col][max_index-row] = temp;

                // swap left vertical
                temp = matrix[max_index-col][row];
                matrix[max_index-col][row] = matrix[max_index-col][max_index-row];
                matrix[max_index-col][max_index-row] = temp;

                println!("swap at pos: ({row},{col})");
                print_matrix(matrix);
            }
        }
    }
}

pub fn print_matrix(matrix: &mut Vec<Vec<i32>>) {
    let size = matrix.len();

    for row in 0..size{
        let row = &matrix[row];
        for col in 0..size{
            let v = row[col];
            print!("{v}");
        }
        println!("");
    }
}
// @lc code=end


/*
 * @lc app=leetcode id=4 lang=rust
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // median is the point where the number of all values (in both arrays) greater is equal to
        // the number of lesser values
        // eg: Input: nums1 = [1,2], nums2 = [3,4]
        // if we started with 2 we'd have 1 less in nums1 and 2 greater in nums2
        // so we'd have to "move up"
        // we can cheat by counting the total number of items if its odd we know we'd actually point at a value
        // otherwise the median will be between two values (which could be the same value) so we point to both values

        // simple algo - start at the mid point of the first array.
        // we binary search the second to find where it lands then count values.
        // so for Input: nums1 = [1,2], nums2 = [3,4]
        // we'd start at index 0,1 for a value of 1.5
        // we'd eventually find its greater than all values in this array for a total of 3 greater one less
        // we know we need to move up one unit to balance so we check index 1,2 ?

        // so for Input: nums1 = [1,2,3], nums2 = [2,3,4]
        // looks at 1-2 or 2.5
        // 2 less and 1 more in the first array and 2 more 1 less in the second
        
        // so for Input: nums1 = [1,2,3], nums2 = [2,3]
        // odd so one number
        // index 1 value 2
        // one less one more in first and one more no less in second
        // thats a pass? I guess
        // so if its odd then as long as its within 2 it means we hit.

        let total_length = nums1.len() + nums2.len();
        let mut guess: f64 = 0.0;
        let mut nums1_diff = 0; // we assume its even by default
        if total_length % 2 == 0{
            // even
            guess = f64::from(nums1[nums1.len()/2-1]+nums1[nums1.len()/2]) * 0.5;

            if nums1.len() % 2 != 0 {
                // if we split nums1 and there are odd digits we will favor the end eg: [1,2,3] we'd have selected 2.5
                nums1_diff = -1;
            }
        }
        else{
            guess = nums1[nums1.len()/2].into();
            if nums1.len() % 2 == 0 {
                // alternatively if the overall length is odd (so we select one value)
                // but this array has an even number of values we'd ALSO favor the end. ha
                nums1_diff = -1;
            }
        }
        return guess;


        
    }
}
// @lc code=end


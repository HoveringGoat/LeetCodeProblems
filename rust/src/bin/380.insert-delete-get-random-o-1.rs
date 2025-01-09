/*
 * @lc app=leetcode id=380 lang=rust
 *
 * [380] Insert Delete GetRandom O(1)
 */

// @lc code=start
use rand::Rng;
use std::collections::HashSet;
struct RandomizedSet {
    set: HashSet<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {
    fn new() -> Self {
        RandomizedSet{
            set: HashSet::new(),
        }
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if (self.set.contains(&val)){
            return false;
        }
        self.set.insert(val);
        return true;
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if (self.set.contains(&val)){
            self.set.remove(&val);
            return true;
        }

        return false;
    }
    
    fn get_random(&self) -> i32 {
        let size: usize = self.set.len();
        let num: usize = rand::thread_rng().gen_range(0..size);
        return *(self.set.iter().collect::<Vec<_>>()[num]);
    }
}

// @lc code=end


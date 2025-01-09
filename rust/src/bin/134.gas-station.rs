/*
 * @lc app=leetcode id=134 lang=rust
 *
 * [134] Gas Station
 */

use core::num;

// @lc code=start
impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let mut min = 100;
        let mut min_station = 0;
        let mut current_gas = 0;
        let num_stations = gas.len();
        for i in 0..num_stations{
            // add gas
            // minus cost to next station
            // record current gas level for station i+1
            current_gas += gas[i];
            current_gas -= cost[i];

            if (current_gas < min){
                min = current_gas;
                min_station = (i + 1) % num_stations;
            }
        }

        // we dont have enough gas to do the circuit
        if (current_gas < 0) {
            return -1;
        }

        return min_station as i32;
        
    }
    pub fn can_complete_circuit_mymethod(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let mut min = 100;
        let mut min_station = 0;
        let mut current_gas = 0;
        let num_stations = gas.len();
        for i in 0..num_stations{
            // add gas
            // minus cost to next station
            // record current gas level for station i+1
            current_gas += gas[i];
            current_gas -= cost[i];

            if (current_gas < min){
                min = current_gas;
                min_station = (i + 1) % num_stations;
            }
        }

        // we dont have enough gas to do the circuit
        if (current_gas < 0) {
            return -1;
        }

        return min_station as i32;
        
    }
}
// @lc code=end


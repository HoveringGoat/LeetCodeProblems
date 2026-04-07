#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # format = [sum, nums...] eeg: [7, 1, 2, 4]
        inc_sets = []   
        com_sets = []
        next_sets = []

        nums = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9]

        for i in nums:
            #print(f"processing num: {i}")
            for s in inc_sets:
                #print(f"s: '{s}', i: '{i}")
                # add num to set and duplicate it in sets
                # if we can make a valid completed set move to com_sets

                #  we're over skip
                if s[0] + i > n:
                    #print("over sum")
                    continue

                # we hit the correct sum
                if s[0] + i == n:
                    # makes sure we dont hit it early thats no good
                    if len(s) == k:
                        #print("correct sum, at nums")
                        temp = s[1:]
                        temp.append(i)
                        com_sets.append(temp)
                    continue
                
                # we are under the sum. ensure that we don't have a full set yet
                if len(s) == k:
                    #print("under sum, at nums")
                    continue

                #print("under sum, under nums")
                # under sum and under values we can add it to the set list
                temp = [s[0] + i]
                temp.extend(s[1:])
                temp.append(i)
                next_sets.append(temp)
                
            # done modifying existing sets. add this value as its own set as well
            inc_sets.append([i, i])
            inc_sets.extend(next_sets)
            next_sets = []
        
        return com_sets
        
# @lc code=end


#
# @lc app=leetcode id=2749 lang=python3
#
# [2749] Minimum Operations to Make the Integer Zero
#
from typing import *
import math
# @lc code=start
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        # target = 10

        # i = [0, 60]
        # n = 2
        # t - (2^i + n) = 0

        #2^i is ALWAYS positive so it will always increase
        # EXCEPT if num2 < 0 we can move in the negative direction
        # if num2 > 0 then we can only decrease
        # create map with i values 
        # use those values to make num1

        values = []
        for i in range(61):
            z = int(math.pow(2, i))
            a = z + num2
            values.append(a)
        
        minValue = values[0]
        
        # if n2 < 0 then there will always be a solution
        if minValue > num1:
            return -1
        
        # now reduce to 0 asap
        # dont both reducing more than min

        # if n2 is even and n1 is odd we HAVE to use the first value
        # since subtracting an even from an even will be even
        # order does not matter.

        # n1 = 3
        # n2 = -12
        # v = [-11, -10, -8, -4, 4, 20, 52, 116]

        # have to use -11. we need to make 14 now
        # -11, -10, 20, 4

        # we want to do an inside out search. If we used to 52 value or higher we KNOW to hit 14
        # we would have to sub -11 at least 3 times to bring us in the range of simliar values.
        # its minimum cost to use is +4 where the others might only be +1
        # 20 makes the most sense as its the closest to 14 (our current value)
        # new value of -6 we can get close with 4 but no way to get closer so its a dead end? (-2)
        # back up and check values around
        # -6-11, -6-10, -6-8, -6-4: -17, -16, -14, -10
        # we have a -10 so we're done. We would need to keep in mind our depth and expand to larger
        # init values as we expand search. So if we didnt find a value this turn or next we'd have to
        # expand search to 52. 126 is a long ways off so another fwe turns to search with these values



        # we need to know what to skip the bigly negative numbers if num2 is very negative.
        # we end up with too many values we are looking through 
        searchDepth = 1
        previousSearchValues = {0}
        previouslyUsedValues = set()
        currSearchValues = set()
        while True:
            for p in previousSearchValues:
                for v in values:
                    currentValue = p+v
                    if currentValue in previouslyUsedValues:
                        continue
                    # compare to num2
                    # if currentValue < minValue:
                    #     # numbers are too smol search next
                    #     continue
                    if currentValue == num1:
                        return searchDepth
                    # this might be invalid logic
                    if currentValue > num1:
                        # numbers are too big search next
                        break
                    currSearchValues.add(currentValue)
                    previouslyUsedValues.add(currentValue)
            previousSearchValues = currSearchValues
            currSearchValues = set()
            searchDepth += 1
            # shouldnt happen but dummy check to make sure not in infinite loop
            if len(previousSearchValues) == 0:
                break
        
        return -1
            

if __name__ == "__main__":
    print("Hello, World!")
    num1 = 17
    num2 = -65
    Solution.makeTheIntegerZero(None, num1, num2)
        
# @lc code=end


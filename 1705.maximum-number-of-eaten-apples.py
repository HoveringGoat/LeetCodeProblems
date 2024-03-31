#
# @lc app=leetcode id=1705 lang=python3
#
# [1705] Maximum Number of Eaten Apples
#

# @lc code=start
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # first lets create a list of all the expiration dates. 
        # we also create a dict of these dates to the amount of apples that expire on that date.
        # once we've created this we can order the expiration dates so theyre all in order
        # then walk through and see how many apples we can eat before all apples expire.

        appleCounts = {}
        finalDatedApples = 0
        for day in range(len(apples)):
            # check if we have apples on this day
            if (apples[day] > 0):
                # calculate these apples expiration date
                expirationDate = day + days[day]

                # check if we have other apples on this date
                if expirationDate in appleCounts.keys():
                    appleCounts[expirationDate] += apples[day]
                else:
                    appleCounts[expirationDate] = apples[day]

        day = 0
        applesEaten = 0
        # we need to keep track of which apples we are currently eating.
        # this value cannot be less than the current day counter.
        applesDated = 0 
        while len(appleCounts.keys()) > 0:
            if applesDated < day:
                applesDated += 1
                continue
            # make sure there are some apples to eat here
            if day in appleCounts.keys() and appleCounts[day] > 0:
                # found apples to eat. yay
                day += 1
                applesEaten += 1

                # if its the last apple or the apples will expire lets remove them
                if appleCounts[applesDated] == 1 or day == applesDated:
                    del appleCounts[applesDated]
                    applesDated += 1
                    continue
                
                appleCounts[applesDated] -= 1
            else:
                # we ate all the apples from that expiration. Lets move along.
                applesDated += 1
        return applesEaten
        
# @lc code=end


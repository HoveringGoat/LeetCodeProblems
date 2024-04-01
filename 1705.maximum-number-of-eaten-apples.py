#
# @lc app=leetcode id=1705 lang=python3
#
# [1705] Maximum Number of Eaten Apples
#

# @lc code=start
from typing import List

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # first lets create a list of all the expiration dates. 
        # we also create a dict of these dates to the amount of apples that expire on that date.
        # once we've created this we can order the expiration dates so theyre all in order
        # then walk through and see how many apples we can eat before all apples expire.

        appleCounts = {}
        finalExpiration = 0
        dayIndex = 0
        applesEaten = 0
        applesDated = 0

        while dayIndex < len(apples) or dayIndex < finalExpiration:
            # if its a day we could generate apples lets check that
            if dayIndex < len(apples):
                # check if we have apples on this day
                if (apples[dayIndex] > 0):
                    # calculate these apples expiration date
                    expirationDate = dayIndex + days[dayIndex]

                    # check if these expire before some other apples we're currently eating
                    if expirationDate < applesDated:
                        applesDated = expirationDate
                        
                    # record final apple expiration date
                    if expirationDate > finalExpiration:
                        finalExpiration = expirationDate

                    # check if we have other apples on this date
                    if expirationDate in appleCounts:
                        appleCounts[expirationDate] += apples[dayIndex]
                    else:
                        appleCounts[expirationDate] = apples[dayIndex]
                        
            # start walkthrough of eating apples. If we want to calculate all dates then walk
            # we won't know when the apples are created. If we do it at the same time we know
            # that the apples will exist
                        
            # days start at 1 not 0            
            day = dayIndex + 1
            if applesDated < day:
                applesDated = day
            
            # look for some good apples
            while applesDated not in appleCounts or appleCounts[applesDated] == 0:
                if applesDated > finalExpiration:
                    break
                applesDated += 1

            if applesDated <= finalExpiration:
                # found apples to eat. yay
                applesEaten += 1
                appleCounts[applesDated] -= 1

            # cant slow the inevitable passage of time
            dayIndex += 1

        return applesEaten
    
    
# if __name__ == '__main__':
#     apples = [1,2,3,5,2]
#     days = [3,2,1,4,2]
#     Solution.eatenApples(None, apples, days)
        
# @lc code=end


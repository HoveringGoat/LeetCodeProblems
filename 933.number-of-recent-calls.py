#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
class RecentCounter:

    pings = []
    index = 0

    def __init__(self):
        self.pings = []
        self.index = 0
        pass

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings[self.index] + 3000 < t:
            self.index += 1
        
        if self.index > 100:
            self.pings = self.pings[self.index:]
            self.index = 0

        return len(self.pings) - self.index


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end


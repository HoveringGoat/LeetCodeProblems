#
# @lc app=leetcode id=2166 lang=python3
#
# [2166] Design Bitset
#

# @lc code=start
class Bitset:

    bitArray = []
    def __init__(self, size: int):
        self.bitArray = []
        for i in range(size):
            self.bitArray.append(False)

    def fix(self, idx: int) -> None:
        self.bitArray[idx] = True

    def unfix(self, idx: int) -> None:
        self.bitArray[idx] = False

    def flip(self) -> None:
        for i in range(len(self.bitArray)):
            self.bitArray[i] = not self.bitArray[i]

    def all(self) -> bool:
        for i in range(len(self.bitArray)):
            if self.bitArray[i] == False:
                return False
        return True
        

    def one(self) -> bool:
        for i in range(len(self.bitArray)):
            if self.bitArray[i] == True:
                return True
        return False

    def count(self) -> int:
        counter = 0
        for i in range(len(self.bitArray)):
            if self.bitArray[i] == True:
                counter += 1
        return counter

    def toString(self) -> str:
        string = ""
        for i in range(len(self.bitArray)):
            if self.bitArray[i] == True:
                string += '1'
            else:
                string += '0'
        return string
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
# @lc code=end


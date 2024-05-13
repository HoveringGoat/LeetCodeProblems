#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        # s is all lowercase

        # this is the promotions problem!!


        #do in one shot. track if a vowel is added and when it should be removed
        max = 0
        sum = 0
        # would be better to have a linked list of k elements. (memory)
        l = [False]*k
        for i,v in enumerate(s):
            if l[i]:
                sum -= 1
            if v in vowels:
                sum += 1
                l.append(True)
                if sum > max:
                    max = sum
                continue
            l.append(False)

        return max



        # dict method is slower
        # d = {}

        # for i, v in enumerate(s):
        #     if v in vowels:
        #         for j in range(i,i+k):
        #             if j >= len(s):
        #                 break
        #             if j in d:
        #                 d[j] += 1
        #             else:
        #                 d[j] = 1
        # max = 0
        # for v in d.values():
        #     if v > max:
        #         max = v
        # return max


        # dumb brute force. Too slow.
        # startIndex = 0
        # endIndex = k
        # max = 0
        # while endIndex <= len(s):
        #     v = 0
        #     substring = s[startIndex:endIndex]
        #     for c in substring:
        #         if c in vowels:
        #             v += 1
        #     if v > max:
        #         max = v
        #     startIndex += 1
        #     endIndex += 1
        # return max
        
# @lc code=end


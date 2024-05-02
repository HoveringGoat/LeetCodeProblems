#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pStack = [p]
        qStack = [q]
        while len(pStack) > 0 and len(qStack) > 0:
            p = pStack.pop()
            q = qStack.pop()

            if p == None and q == None:
                continue

            if p == None or q == None:
                return False

            if p.val != q.val:
                return False
            
            pStack.append(p.left)
            pStack.append(p.right)
            qStack.append(q.left)
            qStack.append(q.right)

        return True
        
# @lc code=end


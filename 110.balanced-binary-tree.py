# @before-stub-for-debug-begin
from python3problem110 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    balanced = True

    def getHeight(self, node: Optional[TreeNode]):
        left = 0
        right = 0
        if node == None:
            return 0

        if node.left != None:
            left = self.getHeight(node.left) + 1

        if node.right != None:
            right = self.getHeight(node.right) + 1

        if abs(left - right) > 1:
            self.balanced = False

        return max(left, right)



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.getHeight(root)
        return self.balanced
        
# @lc code=end


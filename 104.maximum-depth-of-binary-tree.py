#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDepth(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        left = self.getDepth(node.left)
        right = self.getDepth(node.right)

        return max(left, right)+1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
        
# @lc code=end


#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self, node: Optional[TreeNode]):
        if node == None:
            return
        t = node.left
        node.left = node.right
        node.right = t

        self.reverse(node.left)
        self.reverse(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # reverse all left and right nodes
        self.reverse(root)

        return root

        
        
# @lc code=end


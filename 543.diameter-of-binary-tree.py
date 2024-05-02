#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 0 1 1
class Solution:
    def getLengths(self, node: Optional[TreeNode]) -> [int,int,int]:

        leftMax = 0
        rightMax = 0
        leftLength = 0
        rightLength = 0

        if node.left != None:
            leftLengths = self.getLengths(node.left)
            leftMax = max(leftLengths[0]+leftLengths[1], leftLengths[2])
            leftLength = max(leftLengths[0] + 1, leftLengths[1] + 1)

        if node.right != None:
            rightLengths = self.getLengths(node.right)
            rightMax = max(rightLengths[0]+rightLengths[1], rightLengths[2])
            rightLength =  max(rightLengths[0] + 1, rightLengths[1] + 1)
        
        m = max(leftMax,rightMax,leftLength+rightLength)
        return (leftLength, rightLength, m)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l = self.getLengths(root)
        return l[2]
        
# @lc code=end


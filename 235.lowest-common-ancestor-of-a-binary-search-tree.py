# @before-stub-for-debug-begin
from python3problem235 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pHistory = []
    qHistory = []
    p = None
    q = None

    def getHistory(self, node: 'TreeNode', history):
        if node == None:
            return
        h = history.copy()
        h.append(node)
        if node == self.p:
            self.pHistory = h
        if node == self.q:
            self.qHistory = h

        self.getHistory(node.left, h)
        self.getHistory(node.right, h)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        history = []
        self.p = p
        self.q = q
        self.getHistory(root, history)
        index = 0
        while True:
            if index+1 >= len(self.pHistory):
                return self.pHistory[-1]
            if index+1 >= len(self.qHistory):
                return self.qHistory[-1]
            if self.pHistory[index+1] != self.qHistory[index+1]:
                return self.pHistory[index]
            index += 1
        
# @lc code=end


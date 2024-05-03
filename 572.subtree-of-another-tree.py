# @before-stub-for-debug-begin
from python3problem572 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#idk why not work. Maybe try converting tree to a string rep and check if its a literal substring?

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        foundNode = False
        while len(stack) > 0:
            node = stack.pop()
            if node == None:
                continue

            stack.append(node.left)
            stack.append(node.right)

            if node.val != subRoot.val:
                continue

            # we found a matching value now are the subtrees identical
            # search for subRoot in root
            foundNode = True
            pStack = [node]
            qStack = [subRoot]
            while len(pStack) > 0 and len(qStack) > 0:
                p = pStack.pop()
                q = qStack.pop()

                if p == None and q == None:
                    continue

                if p == None or q == None:
                    foundNode = False
                    break

                if p.val != q.val:
                    foundNode = False
                    break
                
                pStack.append(p.left)
                pStack.append(p.right)
                qStack.append(q.left)
                qStack.append(q.right)
            if foundNode:
                break
        return foundNode
        
# @lc code=end


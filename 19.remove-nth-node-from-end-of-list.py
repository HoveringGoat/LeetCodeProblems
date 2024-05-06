# @before-stub-for-debug-begin
from python3problem19 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:
            return None
        reverse = {}
        
        node = head
        
        while node.next != None:
            reverse[node.next] = node
            node = node.next

        # we can reverse n nodes now and remove the nth value

        while n>0:
            n -= 1
            # we are trying to remove the head node
            # we can instead skip it
            if node not in reverse:
                return node.next
            node = reverse[node]
        
        # at this point node.next is the node we want to remove

        node.next = node.next.next

        return head
        
# @lc code=end


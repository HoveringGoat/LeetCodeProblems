#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # function is expecting us to return the head. So we gotta keep track of it. dumb
        node = head
        while(node != None and node.next != None):
            # if next value is the same cut it out of the chain
            if node.val == node.next.val:
                node.next = node.next.next
                continue
            # move to next node
            node = node.next
            
        return head
# @lc code=end
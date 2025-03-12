# @before-stub-for-debug-begin
from python3problem25 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # walk through each k sublist of nodes. reverse each connection.
        # keep ref to first node since it will be the "end" of the sublist
        # when we reach the end of a sublist connect the "first" node from before
        # if its the first sublist that node will be the head
        # if we reach the end of the list in the middle of a sublist go back and reverse it

        # trivial case
        if k == 1:
            return head

        newHead: Optional[ListNode]
        index = 0
        current = head
        last: Optional[ListNode] = None
        nextLast = head
        prev = None
        

        while current != None:
            index += 1
            #print(f"index: {index}")
            #print(f"value: {current.val}")
            next = current.next

            if index == k:
                # kth node - last in the sublist
                # first node in the reversed sublist
                # connect the PREVIOUS sublist "last" node
                
                current.next = prev
                if last == None:
                    newHead = current
                else:
                    last.next = current
                last = nextLast
                index = 0
                
                current = next
                continue


            if index == 1:
                # 1st node in sublist
                # will be the last node in the reversed sublist
                nextLast = current
                current.next = None
                # dont set this node next pointer to the prev node
            else:
                # point current node at previous node. Set current node to next node
                current.next = prev
            
            prev = current
            current = next

        if index != 0:
            current = prev
            while current != None:
                next = current.next
                if current == prev:
                    # the last node terminates
                    current.next = None
                else:
                    current.next = prev
                prev = current
                current = next

            # set last sublist end node to the start of this partial sublist.
            last.next = prev

        return newHead

        # debug print modified list
        current = newHead
        while current != None:
            print(f"{current.val}")
            current = current.next

        
        
# @lc code=end


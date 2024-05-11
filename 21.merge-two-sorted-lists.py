#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # walk along linked lists.
        # if a <= b point last node to a else point to b
        # whichever node gets used move that list along and save it as the "last" node
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        # init last and head values
        last = list1
        head = list1
        if list2.val < list1.val:
            last = list2
            head = list2
            list2 = list2.next
        else:
            list1 = list1.next

        # walk through lists and build new list
        while list1 != None or list2 != None:
            if list2 != None:
                if list1 == None or list2.val < list1.val:
                    last.next = list2
                    last = list2
                    list2 = list2.next
                    continue
            last.next = list1
            last = list1
            list1 = list1.next
        
        return head



        
# @lc code=end


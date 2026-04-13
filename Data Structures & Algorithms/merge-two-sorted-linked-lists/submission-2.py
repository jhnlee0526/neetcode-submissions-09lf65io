# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursion (iteration is better space-wise)
        #   Time : O(n + m)
        #       - n = length of list1
        #       - m = length of list2
        #       - each node is visited once
        #   Space: O(n + m)
        #       - due to recursion stack (not in-place)

        # edge case / base case
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            # merge rest and attach to list1.next
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # merge rest and attach to list2.next
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # linked list - iteratively
        #   time : O(n + m), lengths of list1 & list2
        #   space: O(1)

        dummy = ListNode()  # Null -> 
        cur = dummy         # put a 'cur' pointer at Null

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 or list2

        return dummy.next   # Null -> [list1 -> list2 -> ... -> list]


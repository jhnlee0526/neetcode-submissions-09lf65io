# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # linked list - two pointers
        #   time : O(n), where n is the length of head
        #   space: O(1), constant space

        # Create a dummy node pointing to 'head'
        dummy = ListNode(0, head)

        # Initialize two pointers:
        #   'l' starts at dummy (one node BEFORE head)
        #   'r' starts at head (first actual node)
        l, r = dummy, head

        # Move 'r' forward by 'n' steps to create a gap of 'n' between 'l' and 'r'
        for _ in range(n):
            r = r.next

        # Move both pointers forward together until 'r' reaches the end
        #   At this point, 'l' will be just BEFORE the node to remove
        while r:
            l = l.next
            r = r.next

        # Remove the target node by skipping it in the list
        l.next = l.next.next

        # Return the new head
        return dummy.next
        


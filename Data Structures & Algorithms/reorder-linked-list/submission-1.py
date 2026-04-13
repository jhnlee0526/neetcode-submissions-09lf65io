# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # linked list - reverse & merge
        #   time : O(n)
        #   space: O(1)

        # [Step 1] Find the middle of the list using slow and fast pointers
        # slow moves 1 step, fast moves 2 steps — when fast hits the end, slow is in the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # [Step 2] Reverse the second half of the list
        # Start from the node after the middle, and flip the arrows
        second = slow.next  # Store the second half in 'second'
        slow.next = None    # Cut the list in half
        prev = None
        while second:
            tmp = second.next       # Save the next node
            second.next = prev      # Reverse the pointer
            prev = second           # Move prev forward
            second = tmp            # Move second forward
            # -> prev is now at head of the second half, second is Null

        # [Step 3] Merge the two halves — one from the front, one from the back
        first, second = head, prev  # 'second' is now the head of the reversed half
        while second:                   # b/c the second half is likely shorter than or equal to the first half
            tmp1, tmp2 = first.next, second.next  # Save next nodes
            first.next = second                   # Link first → second
            second.next = tmp1                    # Link second → next of first
            first, second = tmp1, tmp2            # Move both pointers forward

        


        
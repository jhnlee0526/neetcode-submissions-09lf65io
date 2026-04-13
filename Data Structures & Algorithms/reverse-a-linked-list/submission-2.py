# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursion (iteration is better space-wise)
        #   Time : O(n)
        #   Space: O(n)

        # edge case / base case
        if not head:
            return None
        
        cur = head
        if head.next:
            cur = self.reverseList(head.next)   # move cur to next
            head.next.next = head               # reverse the arrow
        head.next = None    # terminate the tail

        return cur          # return new head
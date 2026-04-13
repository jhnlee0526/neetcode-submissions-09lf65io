# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # linked list - recursively (iteration is better space-wise)
        #   time : O(n)
        #   space: O(n)

        if not head:            # edge case / base case: empty list
            return None

        cur = head                  # start with current node
        if head.next:               # if there's a next node, keep going
            cur = self.reverseList(head.next)
            head.next.next = head   # reverse the arrow: head -> head
        head.next = None            # terminate the tail: head -> Null

        return cur                  # return new head (last node of original list)
        

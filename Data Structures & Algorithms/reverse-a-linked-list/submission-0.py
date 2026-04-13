# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # linked list - iteratively
        #   time : O(n)
        #   space: O(1)

        prev, cur = None, head   # put pointers at Null and head: Null(prev) -> head(cur) -> next
        
        while cur:
            temp = cur.next
            cur.next = prev      # reverse the arrow: Null(prev) <- head(cur) -> next

            prev = cur           # Move 'prev' forward to the current node
            cur = temp           # Move 'cur' forward to the next node (originally cur.next)

        return prev              # 'cur' is at Null. 'prev' now points to the new head of the reversed list

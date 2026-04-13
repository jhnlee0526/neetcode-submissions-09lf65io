# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Hashset Detection
        #   Time : O(n)
        #       - n = number of nodes
        #       - each node visited once
        #   Space: O(n)
        #       - stores visited nodes in a set

        visits = set()   # {node1, ..}
        
        cur = head
        while cur:
            if cur in visits:   # Cycle detected!
                return True
            visits.add(cur)
            cur = cur.next
        
        return False
            
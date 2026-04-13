# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointers (slow, fast) - better than hashset space-wise
        #   Time : O(n)
        #   Space: O(1)

        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

        #---------------------
        # Hashset Detection (two pointers is better space-wise)
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
            
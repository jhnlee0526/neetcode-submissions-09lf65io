# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute-force w/ array + two pointers
        #   Time : O(n)
        #       - traverse list once to fill array
        #       - reorder in one pass
        #   Space: O(n)
        #       - stores all nodes in array

        if not head:
            return None
        
        nodes = []
        
        # Fill in nodes
        cur = head
        while cur:      
            nodes.append(cur)
            cur = cur.next
        
        # Re-ordering using two pointers
        l, r = 0, len(nodes) - 1
        while l < r:    
            nodes[l].next = nodes[r]    # link left → right
            l += 1
            if l >= r:
                break
            nodes[r].next = nodes[l]    # link right → left
            r -= 1

        # Terminate the list
        nodes[r].next = None    # prevent cycle
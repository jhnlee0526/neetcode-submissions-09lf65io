# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # linked list - brute force
        #   time : O(n)
        #   space: O(n)

        if not head:            # edge case
            return None
        
        nodes = []
        cur = head
        while cur:              # fill up the nodes list
            nodes.append(cur)
            cur = cur.next
        
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:  ##
                break
            nodes[j].next = nodes[i]
            j -= 1
        
        nodes[i].next = None    # i and j are at the same index 
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Reverse 2nd half & merge w/ two pointers (slow, fast)
        #   Time : O(n)
        #   Space: O(1)

        # Find the middle of the list w/ two pointers (slow, fast)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next    # slow will be in the middle
            fast = fast.next.next


        # Reverse the 2nd half
        second = slow.next  # store the 2nd half
        slow.next = None        # cut the list in half
        
        prev = None             # new head for the 2nd half
        while second:
            temp = second.next
            second.next = prev  # reverse the arrow

            prev = second       # move prev to the next
            second = temp       # move second to the next


        # Merge the 1st & 2nd halves
        first, second = head, prev
        while second:   # b/c len(2nd half) <= len(1st half)
            temp1, temp2 = first.next, second.next
            first.next = second             # link first -> second
            second.next = temp1             # link second -> first's next
            
            first, second = temp1, temp2    # move both pointers to the next


        # #------------------------
        # # Brute-force w/ array + two pointers
        # #   Time : O(n)
        # #       - traverse list once to fill array
        # #       - reorder in one pass
        # #   Space: O(n)
        # #       - stores all nodes in array

        # if not head:
        #     return None
        
        # nodes = []
        
        # # Fill in nodes
        # cur = head
        # while cur:      
        #     nodes.append(cur)
        #     cur = cur.next
        
        # # Re-ordering using two pointers
        # l, r = 0, len(nodes) - 1
        # while l < r:    
        #     nodes[l].next = nodes[r]    # link left → right
        #     l += 1
        #     if l >= r:
        #         break
        #     nodes[r].next = nodes[l]    # link right → left
        #     r -= 1

        # # Terminate the list
        # nodes[r].next = None    # prevent cycle
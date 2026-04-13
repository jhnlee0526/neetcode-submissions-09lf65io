# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## [Linked List Addition] Iteratively
        #### Time Complexity: O(max(n, m)) → We traverse both lists once
        #### Space Complexity: O(max(n, m)) → New linked list is created for output

        # Step 1: Initialize a dummy node to simplify linked list operations
        dummyNode = ListNode()  # Placeholder node for easy list manipulation
        currNode = dummyNode  # Pointer to build the result linked list
        carry = 0  # Variable to store carry-over from addition

        # Step 2: Traverse both linked lists while there are values to process
        while l1 or l2 or carry:
            # Fetch the value from each list node (if exists, otherwise use 0)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Step 3: Compute the sum of the current node values and the carry
            total = val1 + val2 + carry  # Sum of both digits + carry
            
            # Step 4: Determine the new carry and the digit to store in the node
            carry = total // 10  # Extract carry (integer division by 10)
            remainder = total % 10  # Extract the digit (modulo 10)
            
            # Step 5: Append the computed digit as a new node in the result list
            currNode.next = ListNode(remainder)  # Store the single-digit result
            currNode = currNode.next  # Move the pointer forward to continue building
            
            # Step 6: Advance linked list pointers (if applicable)
            l1 = l1.next if l1 else None  # Move to next node in l1
            l2 = l2.next if l2 else None  # Move to next node in l2

        # Step 7: Return the final linked list (ignore dummy node)
        return dummyNode.next
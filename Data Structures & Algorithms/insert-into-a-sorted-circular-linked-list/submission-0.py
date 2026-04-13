# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # 🧠 Algorithm:
        # - Iterative traversal of a Circular Linked List
        # - Goal: insert a value into a sorted circular list
        # - Key idea: find correct position using 3 cases
        
        # ⏱️ Time Complexity: O(N)
        # - In worst case, we traverse the entire circular list once
        #
        # 💾 Space Complexity: O(1)
        # - Only one new node is created, no extra data structures
        
        
        # 🔹 Case 0: Empty list
        # Create a new node that points to itself (circular structure)
        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
        
        # 🔹 Initialize traversal pointers
        pre, cur = head, head.next
        
        # Flag to indicate if correct insertion spot is found
        toInsert = False

        while True:
            
            # 🔹 Case 1: Normal sorted position
            # Example: 1 -> 3 -> 5, insert 4 between 3 and 5
            if pre.val <= insertVal <= cur.val:
                toInsert = True

            # 🔹 Case 2: Rotation point (max → min boundary)
            # Example: 3 -> 5 -> 1 -> 2
            #               ↑
            #           pre > cur indicates pivot
            elif pre.val > cur.val:
                
                # Insert if:
                # - insertVal is greater than max (pre.val)
                # - OR insertVal is smaller than min (cur.val)
                if insertVal >= pre.val or insertVal <= cur.val:
                    toInsert = True
            
            # 🔹 If valid position found → insert node
            if toInsert:
                pre.next = Node(insertVal, cur)
                return head

            # 🔹 Move forward in circular list
            pre, cur = cur, cur.next

            # 🔹 If we completed a full cycle
            # Means:
            # - all values are equal OR
            # - no exact position found
            if pre == head:
                break

        # 🔹 Case 3: Fallback insertion
        # Insert anywhere (valid for equal values case)
        pre.next = Node(insertVal, cur)
        
        return head
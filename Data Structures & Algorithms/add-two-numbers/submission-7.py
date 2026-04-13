# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        currNode = dummyNode
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            remainder = sum % 10
            carry = sum // 10

            newNode = ListNode(remainder)   # create the next
            currNode.next = newNode         # set the next
            currNode = currNode.next        # move to the next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyNode.next
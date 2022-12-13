"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        cur = head

        while cur.next:
            cur = cur.next
            count += 1

        cur = head

        for i in range(count//2):
            cur = cur.next

        return cur

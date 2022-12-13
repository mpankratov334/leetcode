"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        cur = head
        while cur.next:
            cur = cur.next
            count += 1
        if n == count:
            return head.next

        if head.next:
            cur = head
            for _ in range(count - n - 1):
                cur = cur.next
            temp = cur.next.next
            cur.next = temp
            
            return head

        else:
            return None

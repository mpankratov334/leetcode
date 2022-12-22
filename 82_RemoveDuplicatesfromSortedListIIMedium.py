"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""
# PAIN
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0, head)
        previous, cur = None, ans
        while cur.next:
            if not cur.next.next: 
                if cur.val == cur.next.val:
                    previous.next = None
                return ans.next
            if cur.next.next.val != cur.next.val:
                previous = cur
                cur = cur.next
            else:
                correct_next = cur.next.next.next
                while correct_next and cur.next.val == correct_next.val:
                    correct_next = correct_next.next 
                cur.next = correct_next
        return ans.next

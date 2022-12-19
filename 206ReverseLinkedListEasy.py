"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recursive_swap_of_neighborhoods(node1, node2):
            if not node2: return node1
            node3 = node2.next
            node2.next = node1
            return recursive_swap_of_neighborhoods(node2, node3)

        new_head = recursive_swap_of_neighborhoods(None, head)
        return new_head

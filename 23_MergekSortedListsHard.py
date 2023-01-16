"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, heads: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ O(count nodes) """
        if not heads: return None
        m = float('inf')
        i = 0
        node = None
        for index, head in enumerate(heads):
            if head and head.val < m:
                i = index
                m = head.val
                node = head
        ans = node
        if heads[i] and heads[i].next:
            heads[i] = heads[i].next
        else:
            heads.pop(i)
        if ans:
            ans.next = self.mergeKLists(heads)
        return ans

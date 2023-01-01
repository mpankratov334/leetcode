"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
      """ time: O(n), space: O(1) """
        cur = root
        descent = None
        last_left = None
        while cur:
            if cur.left:
                if last_left:
                    last_left.next = cur.left
                last_left = cur.left
                if not descent:
                    descent = cur.left
            if cur.right:
                if last_left:
                    last_left.next = cur.right
                last_left = cur.right
                if not descent:
                    descent = cur.right
        
            if cur.next:
                cur = cur.next
            else:
                cur = descent
                descent = None
                last_left = None
        return root

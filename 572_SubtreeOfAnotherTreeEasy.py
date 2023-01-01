"""
Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_equal(self, node1, node2):
        if node1 and node2:
            return node1.val == node2.val and \
                self.is_equal(node1.right, node2.right) and \
                    self.is_equal(node1.left, node2.left)
        return not node1 and not node2

    def isSubtree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if self.is_equal(node1, node2):
            return True
        if node1:
            return self.isSubtree(node1.left, node2) or \
            self.isSubtree(node1.right, node2)
        return False

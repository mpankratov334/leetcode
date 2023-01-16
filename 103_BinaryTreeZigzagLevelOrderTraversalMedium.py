"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """ O(n) """
        if not root: return []
        ans = []
        ans.append([root])
        is_left = False
        while ans[-1]:
            now = []
            if is_left:
                for i in range(len(ans[-1]) - 1, -1 , -1):
                    node = ans[-1][i]
                    if node.left: now.append(node.left)
                    if node.right: now.append(node.right)
            else:
                for i in range(len(ans[-1]) - 1, -1 , -1):
                    node = ans[-1][i]
                    if node.right: now.append(node.right)
                    if node.left: now.append(node.left)
            ans.append(now)
            is_left = not is_left
        ans.pop()
        for now in ans:
            for i in range(len(now)):
                now[i] = now[i].val
        return ans

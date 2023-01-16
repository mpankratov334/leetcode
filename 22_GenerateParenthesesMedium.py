"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recursion(now_str, open, close):
            nonlocal ans
            if len(now_str) == 2 * n:
                ans.append(now_str)
                return
            if open < n:
                recursion(now_str + '(', open + 1, close)
            if close < open:
                recursion(now_str + ')', open, close + 1)
        recursion('(', 1, 0)
        return ans

"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
"""
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        length = len(s)
        ans = []
        digits = {f"{x}" for x in range(10)}
        def backtrack(cur, i):
            while i < length and cur[i] in digits:
                i += 1
            if i == length:
                ans.append(cur)
                return
            backtrack(cur[:i] + cur[i].upper()+ cur[i+1:], i + 1)
            backtrack(cur[:i] + cur[i].lower()+ cur[i+1:], i + 1)
            
        backtrack(s,0)
        return ans

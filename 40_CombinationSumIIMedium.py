"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        1 <= candidates.length <= 100
        1 <= candidates[i] <= 50
        1 <= target <= 30
        """
        ans = []
        def recursion(c, t, path):
            print(c, t, path)
            nonlocal ans
            if t == 0: 
                ans.append(path)
                return
            if t < 1: return
            while len(c) > 0:
                cand = c.pop(0)
                recursion(c.copy(), t - cand, path + [cand])
                for i in range(c.count(cand)):
                    c.remove(cand)
        recursion(candidates, target, [])
        return ans

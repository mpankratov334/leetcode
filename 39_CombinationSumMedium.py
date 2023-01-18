"""
Companies
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """ 
            1 <= candidates.length <= 30
            2 <= candidates[i] <= 40
            All elements of candidates are distinct.
            1 <= target <= 40
        """
        ans = []
        def recursion(c, t, path):
            nonlocal ans
            if t == 0: ans.append(path)
            if t < 2: return
            while len(c) > 0:
                candidate = c[0]
                recursion(c.copy(), t - candidate, path + [candidate])
                c.pop(0)
        recursion(candidates, target, [])
        return ans
                

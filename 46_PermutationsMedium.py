"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      """ O(n! * n) """
        ans = []
        k = len(nums)
        def backtrack(cur, pool):
            if not pool:
                ans.append(cur)
                return
            for el in pool:
                new_pool = pool.copy()
                new_pool.remove(el)
                backtrack(cur + [el], new_pool)
            return 
        
        backtrack([], set(nums))
        return ans
      
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       return permutations(nums)

"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      """ O(C(n,k)) """
        combinations = []
        def backtrack(start, cur):
            if len(cur) == k: 
                combinations.append(cur)
                return
            for el in range(start + 1, n+1):
                backtrack(el, cur + [el])
        backtrack(0, [])
        return combinations
      
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      """ O(k*C(n, k)) """
        return [list(el) for el in combinations([i for i in range(1,n + 1)], k)]

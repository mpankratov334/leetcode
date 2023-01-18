"""
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ O(n!) """
        ans = []
        for i in range(len(nums) + 1):
            ans.extend(combinations(nums, i))
        return ans

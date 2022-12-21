"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    @staticmethod
    def rbinsearch(nums, target):
        r = len(nums) - 1
        l = 0
        while l < r:
            m = (l+r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return r

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        start = Solution.rbinsearch(nums, target)
        if nums[start] != target: return [-1, -1]
        end = Solution.rbinsearch(nums, target + 1)
        if nums[end] != target: return [start, end - 1]
        return [start, end]

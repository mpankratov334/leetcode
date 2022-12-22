"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, 
return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a 
neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
      """ O(log n) """
        l, r = 0, len(nums) - 1
        while l < r:
            m1 = (l + r) // 2
            m2 = m1 + 1
            if nums[m1] > nums[m2]:
                r = m1
            else:
                l = m2
        return l 

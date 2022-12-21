"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ time: O(n*log n) extraspace: O(1) """
        length = len(nums)
        if length == 1: return nums[0]
        nums.sort()
        for i in range(1, length, 2):
            if nums[i] != nums[i - 1]: 
                return nums[i-1]
        return nums[-1]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ time: O(n) extraspace: O(1) """
        x = 0
        for num in nums:
            x ^= num
        return x

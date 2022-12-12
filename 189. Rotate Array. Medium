"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""

def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = (len(nums) - k) % len(nums)
        nums.extend(nums[:k])
        nums[:k] = []

"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float('inf')
        left = 0
        now_sum = 0
        for right, val in enumerate(nums):
            now_sum += val
            while now_sum >= target and left < right:
                minimum = min(minimum, right - left + 1)
                now_sum -= nums[left]
                left += 1
            if now_sum >= target: return 1
        return 0 if minimum == float("inf") else minimum

"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where
the product of all the elements in the subarray is strictly less than k.
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """ O(n) """
        now_product = 1
        left = 0
        cnt = 0
        for right, val in enumerate(nums):
            now_product *= val
            while now_product >= k and left < right:
                now_product /= nums[left]
                left += 1

            if now_product < k:
                cnt +=right - left + 1
        return cnt
            

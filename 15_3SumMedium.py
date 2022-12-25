"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ O(n*n) """
        ans = set()
        nums.sort()
        length = len(nums)
        for i, val in enumerate(nums[:-2]):
            p1 = i + 1
            p2 = length - 1
            while p1 < p2:
                if nums[p1] + nums[p2] == -val:
                    ans.add((val, nums[p1], nums[p2]))
                    p1 += 1
                elif nums[p1] + nums[p2] > -val:
                    p2 -= 1
                else:
                    p1 += 1
        return ans

"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them 
is that adjacent houses have security systems connected and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        nums[-2] = max(nums[-1], nums[-2])
        for i in range(3,len(nums) + 1):
            nums[-i] = max(nums[-i] + nums[-(i - 2)], nums[-(i - 1)])
        return nums[0]
      
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1: return nums[0]
        memory = {i: None for i in range(length)}
        memory[length - 1] = nums[-1]
        memory[length - 2] = max(nums[-2], nums[-1])
        def fib(i):
            nonlocal memory
            if not memory[i] is None: return memory[i]
            memory[i] = max(fib(i + 1), nums[i] + fib(i + 2))
            return memory[i]

        maximum = fib(0)
        return maximum

"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""
class Solution:
    @classmethod
    def rbinsearch(cls, nums, check, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if check(nums, m, target):
                r = m - 1
            else:
                l = m
 
        return l

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        gtr_for_array = lambda nums, m, target: nums[m][0] > target
        gtr = lambda nums, m, target: nums[m] > target
        
        target_array = Solution.rbinsearch(
                              matrix, gtr_for_array, target)
        index = Solution.rbinsearch(
                         matrix[target_array], gtr, target)
        
        return matrix[target_array][index] == target

""""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
""""
def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        delet = []
        for i in range(len(nums)):
            if nums[i] == 0:
                delet.append(i)
        k = 0
        for i in delet:
            nums.pop(i - k)
            k += 1
            nums.append(0)

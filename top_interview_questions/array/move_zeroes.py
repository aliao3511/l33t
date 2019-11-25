class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        not_zero = 0
        current = 0
        while current < len(nums):
            if nums[current] != 0:
                temp = nums[current]
                nums[current] = nums[not_zero]
                nums[not_zero] = temp
                not_zero += 1
            current += 1

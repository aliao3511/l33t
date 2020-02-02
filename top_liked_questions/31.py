class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
    
        """
        
        def reverse(start, nums):
            end = len(nums) - 1
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start+=1
                end-=1            
        
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i-=1
        if i > 0:
            next_largest = len(nums) - 1
            while next_largest >= 0 and nums[next_largest] <= nums[i-1]:
                next_largest-=1
            temp = nums[i-1]
            nums[i-1] = nums[next_largest]
            nums[next_largest] = temp
        reverse(i, nums)

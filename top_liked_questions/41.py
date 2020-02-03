class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # find 1
        if 1 not in nums: return 1
        if len(nums) == 1: return 2
        
        # clean negative numbers and numbers > n + 1
        for i in range(0, len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums) + 1:
                nums[i] = 1
        
        # check to see what is present
        for i in range(0, len(nums)):
            current = abs(nums[i])
            if current == len(nums):
                nums[0] = abs(nums[0]) * -1
            elif current < len(nums):
                nums[current] = abs(nums[current]) * -1
            else:
                continue
            
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i
        if nums[0] > 0: return len(nums)
        return len(nums) + 1

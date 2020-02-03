class Solution:
    
    def findIndex(self, nums, target, left):
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                end = mid
            else:
                start = mid + 1
        return start
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findIndex(nums, target, True)
        
        if left >= len(nums) or nums[left] != target:
            return [-1,-1]
    
        right = self.findIndex(nums, target, False)
        return [left, right - 1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for idx, num in enumerate(nums):
            reciprocal = target - num
            if reciprocal in indices:
                return [indices[reciprocal], idx]
            else:
                indices[num] = idx

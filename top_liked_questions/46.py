class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        
        def make_permutations(first):
            if first == len(nums):
                permutations.append(nums[:])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                make_permutations(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
            
        make_permutations(0)
        return permutations

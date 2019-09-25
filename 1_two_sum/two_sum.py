class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {} 
        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], idx]
            seen[num] = idx
        return []

# time complexity:
# O(N) - iterate through list, getting and setting in a dict is avg O(1)


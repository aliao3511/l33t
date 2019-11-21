class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse();
        reverse(0, (k % len(nums)) - 1, nums)
        reverse(k, len(nums) - 1, nums)

def reverse(start, end, nums):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1

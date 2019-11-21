class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:  
    uniq = 0
    idx = 1
    current = None
    while idx < len(nums):
      if nums[idx] == current:
        del nums[idx]
        uniq += 1
      else:
        current = nums[idx]
        idx += 1
    return nums

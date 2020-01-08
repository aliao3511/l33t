class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:  
    # uniq = 0
    # idx = 1
    # current = None
    # while idx < len(nums):
      # if nums[idx] == current:
        # del nums[idx]
        # uniq += 1
      # else:
        # current = nums[idx]
        # idx += 1
    # return nums
    if len(num) == 0: return 0
    uniq = 0
    for idx in range(1, len(nums)):
        if (nums[idx] != nums[uniq]):
            uniq += 1
            nums[uniq] = nums[idx]
    return uniq + 1


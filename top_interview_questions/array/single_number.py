class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    # xor operator
        # single = 0
        # for num in nums:
            # single ^= num
        # return single

    # hash
    hash = {}
    for num in nums:
      if num in hash:
        hash.pop(num)
      else:
        hash[num] = 0
    return hash.popitem()[0]

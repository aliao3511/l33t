def rotate(nums, k):
  k = k % len(nums)
  cycle_count = 0
  start = 0
  while cycle_count < len(nums):
    prev = nums[start]
    current = start
    while True:
      next = (current + k) % len(nums)
      temp = nums[next]
      nums[next] = prev
      prev = temp
      current = next
      cycle_count += 1
      if (current == start):
          breakpoint();
          start += 1 
          break
      if (cycle_count >= len(nums)): break

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)

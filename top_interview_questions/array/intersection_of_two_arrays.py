from collections import defaultdict

class Solution:
    # if not sorted 
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # to_hash = nums2 if len(nums1) > len(nums2) else nums1
        # other = nums2 if to_hash == nums1 else nums1
        # hash_counts = defaultdict(lambda: 0)
        # for idx, num in enumerate(to_hash):
            # hash_counts[num] += 1
  
        # intersection_count = 0
        # for num in other:
            # if hash_counts[num] > 0:
                # to_hash[intersection_count] = num
                # intersection_count += 1
                # hash_counts[num] -= 1
            
        # return to_hash[:intersection_count]

    # if inputs sorted or need return value to be sorted
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
	nums1.sort()
	nums2.sort()
	idx1 = 0
	idx2 = 0
	intersection_count = 0
	while idx1 < len(nums1) and idx2 < len(nums2):
	    if nums1[idx1] > nums2[idx2]:
	        idx2 += 1
	    elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else: # numbers the same
	        nums1[intersection_count] = nums1[idx1]
		intersection_count += 1
		idx1 += 1
		idx2 += 1
	return nums1[:intersecion_count] 

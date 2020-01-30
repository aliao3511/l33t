class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        while end > start:
            current_area = (end - start) * min(height[end], height[start]) 
            max_area = current_area if current_area > max_area else max_area
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return max_area

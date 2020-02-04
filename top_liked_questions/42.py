class Solution:
    def trap(self, height: List[int]) -> int:
'''        
        if not height:
            return 0
        left_max = [None for _ in range(len(height))]
        right_max = [None for _ in range(len(height))]
        area = 0
        
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i - 1])
        
        right_max[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
            
        for i in range(len(height)):
            area += min(left_max[i], right_max[i]) - height[i]
        
        return area
'''
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        answer = 0
        while left < right:
            # iterate from left to right
            if height[left] < height[right]: 
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    answer += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    answer += (right_max - height[right])
                right -= 1
        return answer

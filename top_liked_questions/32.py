class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right and left > longest:
                longest = left 
                
            if right > left:
                left = right = 0
        
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right and left > longest:
                longest = left
            
            if left > right:
                left = right = 0
        return longest * 2

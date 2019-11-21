class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(0, s.length):
            len1 = fromCenter(s, i, i) # center on a character
            len2 = fromCenter(s, i, i+1) # center not on a character
            len = max(len1, len2)
            
    
    def fromCenter(s: str, left: int, right: int):
        while left >= 0 and right < s.length and s[l] == s[r]:
            left--
            right++
        return right - left - 1

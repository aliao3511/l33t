class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        chars = {}
        for end, ch in enumerate(s):
            if ch in chars:
                start = max(chars[ch] + 1, start)
            longest = max(end - start + 1, longest)
            chars[ch] = end
        return longest

# time complexity: O(N) - iterate through string
# space complexity: O(N) - at most N unique chars within dict

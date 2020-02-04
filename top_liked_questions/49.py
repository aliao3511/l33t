from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            chars = [0 for _ in range(26)]
            for char in s:
                chars[ord(char) - ord('a')] += 1
            anagrams[tuple(chars)].append(s)
        return anagrams.values()

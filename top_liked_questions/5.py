def longestPalindrome(s):
    longest = ''
    for i in range(0, len(s)):
        center1 = fromCenter(s, i, i) # center on a character
        center2 = fromCenter(s, i, i+1) # center not on a character
        contender = center1 if len(center1) > len(center2) else center2
        longest = contender if len(contender) > len(longest) else longest
    return longest

def fromCenter(s, left, right):
    longest = ''
    while left >= 0 and right < len(s) and s[left] == s[right]:
        current = s[left:(right+1)]
        if len(current) > len(longest):
            longest = current
        left-=1
        right+=1
    return longest

# print(longestPalindrome('babad'));
print(longestPalindrome('a'));

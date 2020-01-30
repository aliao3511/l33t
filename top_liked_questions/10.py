def isMatch(s, p):
    # base case: finished iterating through pattern and string
    if not p:
        return not s

    potential_match = bool(s) and p[0] in {s[0], '.'}

    if len(p) >= 2 and p[1] == '*':
        # 1) skip in pattern; 2) keep in pattern (must have either '.' or match)
        return self.isMatch(s, p[2:]) or (potential_match and self.isMatch(s[1:], p)
    )
    else:
        if potential_match:
            return self.isMatch(s[1:], p[1:])
        else:
            return False
# isMatch("aa", "a")
# isMatch("aa", "a*")
isMatch('aab', 'c*a*b')

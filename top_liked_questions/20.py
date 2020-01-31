def isValid(s):
    parentheses = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    open_parentheses = [*parentheses.values()]
    stack = []
    for char in s:
        import pdb; pdb.set_trace()
        if char in open_parentheses: # opening
            stack.append(char)
        else:
            if len(stack) == 0: return False
            popped_char = stack.pop(len(stack - 1))
            if parentheses[char] != popped_char: 
                return False
    return len(stack) == 0

isValid('([)]')

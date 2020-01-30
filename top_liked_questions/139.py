def wordBreak(s, wordDict):
    word_set = set(wordDict)
    seen = set()
    queue = [0]
    while len(queue) > 0:
        start = queue.pop()
        if start in seen:
            continue;
        seen.add(start)
        idx = start + 1
        while idx <= len(s):
            substring = s[start:idx]
            if substring in word_set:
                if idx == len(s): return True
                queue.insert(0, idx)
            idx += 1
    return False

# print(wordBreak('leetcode', ['leet','code']))
# print(wordBreak('catsandog', ['cats','dog','sand','and','cat']))

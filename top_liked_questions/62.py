class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def findPath(x, y, memo):
            if x == 1 and y == 1:
                return 1
            if x <= 0 or y <= 0:
                return 0
            pos = tuple([x, y])
            if pos in memo:
                return memo[pos]
            else:
                memo[pos] = findPath(x - 1, y, memo) + findPath(x, y-1, memo)
                return memo[pos]
        
        return findPath(m, n, {})

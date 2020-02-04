class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = [0] * len(grid[0])
        height = len(grid)
        dp = [row for _ in range(height)]
        
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0:
                    min_distance = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    min_distance = grid[i][j] + dp[i - 1][j]
                else:
                    up = dp[i-1][j]
                    left = dp[i][j-1]
                    min_distance = min(up, left) + grid[i][j]
                dp[i][j] = min_distance
        return dp[len(dp) - 1][len(dp[0]) - 1]

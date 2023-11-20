from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[n - 1] = 1

        # Time: O(n * m), Space: O(n)
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if grid[r][c]:
                    dp[c] = 0
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]


def main():
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstacleGrid)
    print("Output:", result)


if __name__ == "__main__":
    main()

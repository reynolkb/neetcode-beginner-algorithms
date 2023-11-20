from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Initialize a 1D array for dynamic programming with zeros
        dp = [0] * n

        # Set the last element to 1 as a starting point
        dp[n - 1] = 1

        # Iterate through the grid in reverse order (starting from the bottom-right corner)
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                # If the current cell is an obstacle, set its path count to 0
                if grid[r][c]:
                    dp[c] = 0
                # If it's not an obstacle, add the path count from the cell to the right and the cell below
                elif c + 1 < n:
                    dp[c] = dp[c] + dp[c + 1]

        # Return the number of paths to the top-left corner of the grid
        return dp[0]


def main():
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstacleGrid)
    print("Output:", result)


if __name__ == "__main__":
    main()

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        row, column = len(grid), len(grid[0])

        # Initialize a 1D array for dynamic programming with zeros
        dp = [0] * column

        # Set the last element to 1 as a starting point
        dp[column - 1] = 1

        # Iterate through the grid in reverse order (starting from the bottom-right corner)
        for r in reversed(range(row)):
            for c in reversed(range(column)):
                # If the current cell is an obstacle, set its path count to 0
                if grid[r][c]:
                    dp[c] = 0
                # If it's not an obstacle, add the path count from the cell below and the cell to the right
                # dp[c] is the cell below since it is updated outside the inner loop
                elif c + 1 < column:
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

# Define the Solution class
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # Base condition: Stop DFS if we go out of bounds, visit a water cell, or revisit a cell
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0

            # Mark the cell as visited
            visit.add((r, c))

            # Initialize a variable to hold the area of the current island chunk
            area = 1

            # Define possible directions to move in the grid: down, up, right, left
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            # Visit all adjacent cells
            for dr, dc in directions:
                # Accumulate the area returned from visiting each adjacent cell
                area += dfs(r + dr, c + dc)

            # Return the total area for this island chunk
            return area

        # Initialize area to hold the maximum island area
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                # Update maximum island area through DFS traversal
                maxArea = max(maxArea, dfs(r, c))

        # Return the maximum area found
        return maxArea


def main():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    solution = Solution()
    result = solution.maxAreaOfIsland(grid)
    print("Output:", result)


if __name__ == "__main__":
    main()

from typing import List, Set


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check for an empty grid or empty first row
        if not grid or not grid[0]:
            return 0

        # Initialize count of islands
        islands = 0
        # Create a set to track visited cells
        visit = set()
        # Get dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Define the DFS function
        def dfs(r, c):
            # Check boundary conditions, whether the cell is water or already visited
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            # Mark the cell as visited by adding to the set
            visit.add((r, c))

            # Define directions for adjacent cells
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            # Visit all adjacent cells
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate through all cells in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land and has not been visited
                if grid[r][c] == "1" and (r, c) not in visit:
                    # Increment the island count
                    islands += 1
                    # Call DFS starting from this cell
                    dfs(r, c)

        # Return the total number of islands
        return islands


def main():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    solution = Solution()
    result = solution.numIslands(grid)
    print("Output:", result)


if __name__ == "__main__":
    main()

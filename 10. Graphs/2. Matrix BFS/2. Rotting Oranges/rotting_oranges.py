# Define a class named Solution with a method orangesRotting that takes a grid as input
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Create a deque (queue) for storing coordinates of rotten oranges
        q = deque()
        # Counter for fresh oranges
        fresh = 0
        # Time counter initialized to 0
        time = 0

        # Iterate over rows and columns to find rotten and fresh oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # Count fresh oranges
                if grid[r][c] == 1:
                    fresh += 1
                # Add rotten oranges to queue
                if grid[r][c] == 2:
                    q.append((r, c))

        # Define the directions to move in the grid (up, down, left, right)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Loop until there are no fresh oranges or the queue is empty
        while fresh > 0 and q:
            length = len(q)
            # Process each level of rotten oranges in the queue
            for i in range(length):
                r, c = q.popleft()
                # Spread rot to adjacent fresh oranges
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # Check bounds and update fresh to rotten
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            # Increment time counter after each level
            time += 1
        # Return time if no fresh oranges left, otherwise return -1
        return time if fresh == 0 else -1

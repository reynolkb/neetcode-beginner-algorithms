from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Get the length of the grid
        N = len(grid)

        # Initialize a deque with starting point (0,0) and initial length 1
        q = deque([(0, 0, 1)])  # r, c, length

        # Initialize a set to keep track of visited cells
        visit = set((0, 0))

        # Define the directions to move in the grid
        # fmt: off
        directions = [
            [0, 1], [1, 0], [0, -1], [-1, 0], 
            [1, 1], [-1, -1], [1, -1], [-1, 1]
        ]

        # Loop until the deque is empty
        while q:
            # Pop the front element from deque and unpack its values
            r, c, length = q.popleft()

            # Skip if the cell is out of grid or grid[r][c] == 1 since 0 is false and 1 is true
            if min(r, c) < 0 or max(r, c) == N or grid[r][c]:
                continue

            # Check if we reached the destination
            if r == N - 1 and c == N - 1:
                return length

            # Loop through all possible directions
            for dr, dc in directions:
                # Check if the cell is visited
                if (r + dr, c + dc) not in visit:
                    # Append the new cell to deque with incremented length
                    q.append((r + dr, c + dc, length + 1))

                    # Add the new cell to visited set
                    visit.add((r + dr, c + dc))

        # Return -1 if there is no path
        return -1


def main():
    # fmt: off
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    solution = Solution()
    result = solution.shortestPathBinaryMatrix(grid)
    print("Output:", result)


if __name__ == "__main__":
    main()

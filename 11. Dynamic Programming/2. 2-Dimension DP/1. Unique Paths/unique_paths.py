class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the first row with all 1s
        # Each cell represents the number of ways to reach that cell
        row = [1] * n

        for i in range(m - 1):
            # Initialize the new row with all 1s
            newRow = [1] * n
            # Iterate over each cell in the row from right to left, excluding the first cell
            for j in range(n - 2, -1, -1):
                # Calculate the number of paths to the current cell
                # It's the sum of paths from the cell to its right and the cell below it
                newRow[j] = newRow[j + 1] + row[j]
            # Update the current row to be the new row for the next iteration
            row = newRow
        # Return the number of paths to reach the top-left cell
        return row[0]


def main():
    m = 3
    n = 7
    solution = Solution()
    result = solution.uniquePaths(m, n)
    print("Output:", result)


if __name__ == "__main__":
    main()

class Solution(object):
    def searchMatrix(self, matrix, target):
        # Get the dimensions of the matrix
        row, col = len(matrix), len(matrix[0])
        # Initialize pointers for binary search on the flattened matrix
        low, high = 0, row * col - 1
        """
        row = 3
        col = 4
        row * col = 12
        matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 60],
        ]
        flattened matrix = [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
        row * col - 1 = 11th index of flattened matrix
        """

        # Perform binary search
        while low <= high:
            # Calculate the midpoint in the 1D representation of the matrix
            mid = (low + high) // 2
            """ 
            Convert the 1D index 'mid' to its corresponding 2D index in the matrix

            mid // col
            if row = 3, col = 4 and mid = 5, in the flattened version 0-3 are the first row, 4-7 are the second row and 8-11 are the third row
            When you do 5 // 4, it gives you 1, correctly pointing to the second row

            mid % col
            if row = 3, col = 4 and mid = 5, each row in the flattened version has 'col' elements (4 in this case)
            When you do 5 % 4, it gives you 1, correctly pointing to the second col
            """
            mid_val = matrix[mid // col][mid % col]

            # Check if the value at 'mid' is equal to the target
            if mid_val == target:
                return True
            # If the value at 'mid' is less than the target, narrow the search to the right half
            elif mid_val < target:
                low = mid + 1
            # If the value at 'mid' is greater than the target, narrow the search to the left half
            else:
                high = mid - 1

        # If the loop completes without finding the target, return False
        return False

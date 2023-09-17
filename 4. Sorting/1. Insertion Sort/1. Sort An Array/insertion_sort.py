class Solution(object):
    def sortArray(self, nums):
        # Loop starts from the second element to the last element of the array
        for i in range(1, len(nums)):
            # Store the current element as 'key'
            key = nums[i]
            # Initialize a pointer 'j' to the previous element of 'key'
            j = i - 1

            # Shift elements that are greater than 'key' one position ahead
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1

            # Insert the 'key' at its correct position in the sorted section
            nums[j + 1] = key

        # Return the sorted array
        return nums


def main():
    sol = Solution()
    nums = [5, 1, 1, 2, 0, 0]
    res = sol.sortArray(nums)
    print("The sorted list is " + str(res))
    """ 
    1. First, the 'key' starts at index 1 (i.e., nums[1] = 1).
    2. It compares the 'key' with the elements on its left (sorted part).
    3. If the 'key' is smaller, it moves the larger elements one position to the right.
    4. Once the correct position for the 'key' is found, it is inserted.
    5. The process is repeated for each element in the array from index 1 to n-1.
    6. Finally, the array becomes [0, 0, 1, 1, 2, 5] after sorting.
    """


if __name__ == "__main__":
    main()

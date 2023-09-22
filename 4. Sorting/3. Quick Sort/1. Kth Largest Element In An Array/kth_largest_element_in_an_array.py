class Solution(object):
    def findKthLargest(self, nums, k):
        # since we are sorting array in ascending order, we have to update k to reflect the index correctly
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        # Loop until we find the correct position
        while left < right:
            # Find a pivot and partition array around it
            pivot = self.partition(nums, left, right)

            # If the pivot is smaller than k, look in the right partition
            if pivot < k:
                left = pivot + 1
            # If the pivot is larger than k, look in the left partition
            elif pivot > k:
                right = pivot - 1
            # If the pivot equals k, we found the element
            else:
                break

        return nums[k]

    # Function to partition the array for quickselect
    # we swap both nums[fill] with nums[i] and nums[fill] with nums[right] because we are swapping in place
    def partition(self, nums, left, right):
        # Initialize fill pointer and pivot variable
        fill, pivot = left, nums[right]

        # Loop through array to move smaller elements to the left of pivot
        for i in range(left, right):
            if nums[i] <= pivot:
                # Swap elements at 'fill' and 'i' to move smaller elements to the left of the pivot which is set to fill at the end.
                # Then increment 'fill' to prepare for the next smaller element.
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        # Swap the pivot element (initially at 'right') with the element at the 'fill' index.
        # This places the pivot in its correct sorted position, with all smaller elements to its left.
        nums[fill], nums[right] = nums[right], nums[fill]

        # Return the position of the pivot
        return fill


def main():
    nums = [6, 5, 8, 2, 1, 3]
    k = 5
    sol = Solution()
    result = sol.findKthLargest(nums, k)
    print(f"The {k}th largest element is {result}")


if __name__ == "__main__":
    main()

class Solution(object):
    def findKthLargest(self, nums, k):
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

        # Return the kth smallest element, which is the kth largest element
        return nums[k]

    # Function to partition the array for quickselect
    def partition(self, nums, left, right):
        # Initialize pivot and fill variables
        pivot, fill = nums[right], left

        # Loop through array to move smaller elements to the left of pivot
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        # Move the pivot element to its sorted position
        nums[fill], nums[right] = nums[right], nums[fill]

        # Return the position of the pivot
        return fill


def main():
    nums = [9, 7, 5, 3, 1]
    k = 4
    sol = Solution()
    result = sol.findKthLargest(nums, k)
    print(f"The {k}th largest element is {result}")


if __name__ == "__main__":
    main()

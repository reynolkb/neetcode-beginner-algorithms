class Solution(object):
    def sortArray(self, nums):
        def merge(left, right):
            # Initialize an empty list to hold the sorted elements
            result = []
            # Initialize pointers for the left and right arrays
            i, j = 0, 0

            # Loop to compare and merge elements from left and right arrays
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # If there are leftover elements in the left array, extend the result
            result.extend(left[i:])
            # If there are leftover elements in the right array, extend the result
            result.extend(right[j:])

            return result

        # Merge Sort function
        def merge_sort(arr):
            # Base case: if the array has one or zero elements, it's already sorted
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            # Recursively sort the left and right halves
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            # Merge the sorted left and right halves and return
            return merge(left, right)

        return merge_sort(nums)


def main():
    sol = Solution()
    nums = [5, 1, 1, 2, 0, 0]
    res = sol.sortArray(nums)
    print("The sorted list is " + str(res))
    """ 
    1. First merge_sort([5, 1, 1, 2, 0, 0]) is called.
        * left = merge_sort([5, 1, 1])
        * right = merge_sort([2, 0, 0])
    2. For left = merge_sort([5, 1, 1]):
        * left = merge_sort([5]) (base case, returns [5])
        * right = merge_sort([1, 1])
            * left = merge_sort([1]) (base case, returns [1])
            * right = merge_sort([1]) (base case, returns [1])
        * Here, merge([1], [1]) is called and returns [1, 1].
        * Then, merge([5], [1, 1]) is called and returns [1, 1, 5].
    3. For right = merge_sort([2, 0, 0]):
        * left = merge_sort([2]) (base case, returns [2])
        * right = merge_sort([0, 0])
            * left = merge_sort([0]) (base case, returns [0])
            * right = merge_sort([0]) (base case, returns [0])
        * Here, merge([0], [0]) is called and returns [0, 0].
        * Then, merge([2], [0, 0]) is called and returns [0, 0, 2].
    4. Finally, merge([1, 1, 5], [0, 0, 2]) results in [0, 0, 1, 1, 2, 5]

    Once the base case is reached and you start to unwind out of the recursive calls, the merge function is invoked to combine the sorted left and right arrays.
    """


if __name__ == "__main__":
    main()

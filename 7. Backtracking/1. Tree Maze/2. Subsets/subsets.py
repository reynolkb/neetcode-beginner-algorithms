class Solution(object):
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            # Base case: If 'i' is equal to or greater than the length of nums,
            # it means we've finished exploring all numbers in the list.
            if i >= len(nums):
                """
                Append the current state of 'subset' to the result list.
                Using 'subset.copy()' ensures we save the current contents of 'subset' as a new distinct list.
                Without 'subset.copy()', all entries in 'res' would be references to the same 'subset' object.
                This means any subsequent changes to 'subset' would affect all its references in 'res'. The final 'res' would then have multiple instances of the last state of 'subset', likely [[], [], ...].
                """
                res.append(subset.copy())
                return

            # Recursive case 1: Decide to include the current number, nums[i], in the subset.
            # Append the current number.
            subset.append(nums[i])
            # Continue the search with the next index.
            dfs(i + 1)

            # Recursive case 2: Then we decide NOT to include nums[i] in the subset.
            # Remove the last appended number.
            subset.pop()
            # Continue the search with the next index, without the current number.
            dfs(i + 1)

        # Start the DFS traversal from the first number in the list.
        dfs(0)

        return res


def main():
    nums = [1, 2, 3]
    solution = Solution()
    output = solution.subsets(nums)
    print(output)


if __name__ == "__main__":
    main()

class Solution(object):
    def combinationSum(self, candidates, target):
        # The 'res' list will store all valid combinations.
        res = []

        def dfs(i, cur, total):
            # Base case 1: If the total is equal to the target,
            # it means we've found a valid combination.
            if total == target:
                """
                Append the current state of 'cur' to the result list.
                Using 'cur.copy()' ensures we save the current contents of 'cur' as a new distinct list.
                Without 'cur.copy()', all entries in 'res' would be references to the same 'cur' object.
                This means any subsequent changes to 'cur' would affect all its references in 'res'.
                The final 'res' would then have multiple instances of the last state of 'cur'.
                """
                res.append(cur.copy())
                return

            # Base case 2: If 'i' has reached the end of candidates or if the total exceeds the target,
            # it means the current path is not valid, so we return without making further recursive calls.
            if i >= len(candidates) or total > target:
                return

            # Recursive case 1: Decide to include the current candidate, candidates[i], in the combination.
            # Append the current candidate to 'cur'.
            cur.append(candidates[i])
            # Continue the search using the same index 'i' as we can reuse candidates.
            dfs(i, cur, total + candidates[i])

            # Recursive case 2: Decide NOT to include candidates[i] in the combination.
            # Remove the last appended candidate.
            cur.pop()
            # Continue the search with the next index, without the current candidate.
            dfs(i + 1, cur, total)

        # Start the DFS traversal from the first candidate with an initial total of 0 and an empty 'cur' list.
        dfs(0, [], 0)

        return res


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    output = solution.combinationSum(candidates, target)
    print(output)


if __name__ == "__main__":
    main()

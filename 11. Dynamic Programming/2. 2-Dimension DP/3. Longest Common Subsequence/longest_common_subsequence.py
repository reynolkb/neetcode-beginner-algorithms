class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D array 'dp' with dimensions (len(text1)+1) x (len(text2)+1)
        # we add +1 for an extra row and column to act as a buffer later on when we're doing i + 1 and j + 1
        # Initialize all elements to 0. This array will be used for dynamic programming
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            # For each character in text1, iterate over text2 in reverse order
            for j in range(len(text2) - 1, -1, -1):
                # If the current characters in text1 and text2 match
                if text1[i] == text2[j]:
                    # Set dp[i][j] to 1 plus the value of dp[i+1][j+1]
                    # This accounts for the matching character and adds the length of the common subsequence found so far
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # dp[i][j + 1] - keep position for text1, but move to the next character of text2
                    # dp[i + 1][j] - keep position for text2, but move to the next character of text1
                    # pretty much we are taking the max of either substring combination
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # Return the top-left element of the dp array, which contains the length of the longest common subsequence
        return dp[0][0]


def main():
    text1 = "abcde"
    text2 = "ace"
    solution = Solution()
    result = solution.longestCommonSubsequence(text1, text2)
    print("Output:", result)


if __name__ == "__main__":
    main()

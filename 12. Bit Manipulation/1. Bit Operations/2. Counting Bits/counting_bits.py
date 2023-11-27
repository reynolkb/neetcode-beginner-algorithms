from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


def main():
    n = 2
    solution = Solution()
    result = solution.countBits(n)
    print("Output:", result)


"""
Input: 2
Output: [0, 1, 1]

0 in binary is 0. The number of 1's in this binary number is 0.
1 in binary is 1. The number of 1's in this binary number is 1.
2 in binary is 10. The number of 1's in this binary number is 1.
"""

if __name__ == "__main__":
    main()

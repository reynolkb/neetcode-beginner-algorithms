from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize two variables 'rob1' and 'rob2' to 0
        rob1, rob2 = 0, 0

        for n in nums:
            # Calculate the maximum value between 'n + rob1' and 'rob2'
            temp = max(n + rob1, rob2)

            # Update 'rob1' to the value of 'rob2'
            rob1 = rob2

            # Update 'rob2' to the value of 'temp'
            rob2 = temp

        return rob2


def main():
    nums = [1, 2, 3, 1]
    solution = Solution()
    result = solution.rob(nums)
    print("Output:", result)


if __name__ == "__main__":
    main()

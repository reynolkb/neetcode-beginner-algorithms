from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans


def main():
    nums = [1, 3, 2, 1]
    solution = Solution()
    result = solution.getConcatenation(nums)
    print("Concatenation:", result)


if __name__ == "__main__":
    main()

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


def main():
    n = 0o0000000000000000000000000001011
    solution = Solution()
    result = solution.hammingWeight(n)
    print("Output:", result)


if __name__ == "__main__":
    main()

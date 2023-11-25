class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # looks at entire number
        while n:
            # n % 2 returns 0 or 1 as the remainder
            # Since the rightmost bit in binary determines whether the number is odd or even, n % 2 directly tells us the value of the rightmost bit
            res += n % 2
            # shifts all bits of `n` to the right by one position, discarding the rightmost bit and moving the next bit to the rightmost position
            n = n >> 1
        return res


def main():
    n = 0o0000000000000000000000000001011
    solution = Solution()
    result = solution.hammingWeight(n)
    print("Output:", result)


if __name__ == "__main__":
    main()

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res


def main():
    n = 0b0000010100101000001111010011100
    solution = Solution()
    result = solution.reverseBits(n)
    print("Output:", result)


if __name__ == "__main__":
    main()

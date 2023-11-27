class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # Right shifts 'n' by 'i' bits and isolates the rightmost bit value of n. then checks it against 1 to see if both are true
            bit = (n >> i) & 1

            # Left shifts the isolated bit to its reversed position and adds it to 'res'.
            res += (bit << (31 - i))
        return res


def main():
    n = 0b0000010100101000001111010011100
    solution = Solution()
    result = solution.reverseBits(n)
    print("Output:", result)


if __name__ == "__main__":
    main()

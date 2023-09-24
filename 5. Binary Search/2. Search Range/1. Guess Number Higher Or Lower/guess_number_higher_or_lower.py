class Solution(object):
    # Pre-defined API simulation
    def guess(self, num, pick):
        if num > pick:
            return -1
        elif num < pick:
            return 1
        else:
            return 0

    # Function to find the number
    def guessNumber(self, n, pick):
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            result = self.guess(mid, pick)
            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1


def main():
    n = 10
    pick = 6
    sol = Solution()
    result = sol.guessNumber(n, pick)
    print(f"The picked number is: {result}")


if __name__ == "__main__":
    main()

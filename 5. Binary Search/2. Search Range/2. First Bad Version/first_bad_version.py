class Solution(object):
    # Pre-defined API simulation
    def isBadVersion(self, version, bad):
        if version >= bad:
            return True
        else:
            return False

    def firstBadVersion(self, n, bad):
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            badVersion = self.isBadVersion(mid, bad)

            if badVersion:
                high = mid - 1
            else:
                low = mid + 1
        return low


def main():
    n = 5
    bad = 4
    sol = Solution()
    result = sol.firstBadVersion(n, bad)
    print(f"The first bad version is {result}")


if __name__ == "__main__":
    main()

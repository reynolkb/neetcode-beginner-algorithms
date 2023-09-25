import math


class Solution(object):
    # Helper function to find hours needed for a given speed
    def hours_needed(self, speed, piles):
        totalTime = 0
        for pile in piles:
            # math.ceil(pile / speed)
            totalTime += -(-pile // speed)
        return totalTime

    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        # Use low < high when you're searching for a value that meets a condition (min or max).
        # Use low <= high when searching for an exact match in a list.
        while low < high:
            mid = (low + high) // 2
            if self.hours_needed(mid, piles) <= h:
                high = mid
            else:
                low = mid + 1

        return low


def main():
    piles = [3, 6, 7, 11]
    h = 8
    sol = Solution()
    result = sol.minEatingSpeed(piles, h)
    print(f"The min eating speed of bananas per hour is {result}")


if __name__ == "__main__":
    main()

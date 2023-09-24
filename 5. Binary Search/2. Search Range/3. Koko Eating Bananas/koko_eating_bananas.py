import math


class Solution(object):
    # Helper function to calculate hours needed for speed k
    def hours_needed(self, speed, piles):
        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(pile / speed)
        return totalTime

    def minEatingSpeed(self, piles, h):
        low, high = 1, max(piles)
        while low < high:
            mid = (low + high) // 2
            if self.hours_needed(mid, piles) <= h:
                high = mid
            else:
                low = mid + 1

        return low

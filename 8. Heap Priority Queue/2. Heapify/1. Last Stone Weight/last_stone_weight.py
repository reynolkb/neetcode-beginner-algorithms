import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate all stones' weights to use Python's min-heap as a max-heap
        stones = [-s for s in stones]

        # Transform the list into a heap
        heapq.heapify(stones)

        # Continue until one or zero stones are left
        while len(stones) > 1:
            # Pop the heaviest stone (smallest negated value)
            first = heapq.heappop(stones)

            # Pop the second heaviest stone
            second = heapq.heappop(stones)

            # If the second stone is greater than the first, which means less than since they're both negative
            if second > first:
                # Push the remaining weight back into heap
                heapq.heappush(stones, first - second)

        # Append zero for the case where no stones are left
        stones.append(0)

        # Return the weight of the last stone or zero
        return abs(stones[0])


def main():
    stones = [2, 7, 4, 1, 8, 1]
    sol = Solution()
    res = sol.lastStoneWeight(stones)
    print(res)


if __name__ == "__main__":
    main()

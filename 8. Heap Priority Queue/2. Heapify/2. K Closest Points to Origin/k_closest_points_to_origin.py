import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Initialize an empty list to act as a minimum heap for storing distances and points
        minHeap = []

        # Loop through the list of points to calculate their distances from the origin (0, 0)
        # This is a shorthand for unpacking the inner lists similar to for index, x in enumerate(some_list
        for x, y in points:
            # Calculate the distance squared for each point
            dist = (x**2) + (y**2)
            # Append the distance and the point as a tuple to minHeap
            minHeap.append((dist, x, y))

        # Convert the minHeap list into a valid heap data structure (in-place)
        heapq.heapify(minHeap)

        # Initialize an empty list to store the k closest points
        res = []

        # Pop the smallest k distances (and their corresponding points) from the heap
        for _ in range(k):
            # Pop and unpack the smallest distance and point
            _, x, y = heapq.heappop(minHeap)
            # Append the point to the result list
            res.append((x, y))

        # Return the k closest points
        return res


def main():
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    sol = Solution()
    res = sol.kClosest(points, k)
    print(res)


if __name__ == "__main__":
    main()

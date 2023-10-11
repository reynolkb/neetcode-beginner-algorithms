import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize the minHeap with the given list of numbers and store k.
        # self.minHeap = nums and self.k = k since two variables on the left and two variables on the right
        self.minHeap, self.k = nums, k

        # Convert our list into a min-heap.
        # This operation makes the smallest element accessible in O(1) time.
        heapq.heapify(self.minHeap)

        # If the size of our min-heap is greater than k,
        # then pop the smallest elements until its size becomes k.
        # This ensures that our heap always contains the k largest elements seen so far.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add the new value to our min-heap.
        heapq.heappush(self.minHeap, val)

        # If after adding, the size of our min-heap becomes greater than k,
        # pop the smallest element. This ensures size constraint and
        # that the heap contains the k largest elements.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The 0th element of our min-heap (the root) is the kth largest element.
        # We return it as the result.
        return self.minHeap[0]

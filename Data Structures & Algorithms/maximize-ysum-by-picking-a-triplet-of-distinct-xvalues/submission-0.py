class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        # Hashmap + Maxheap
        ## Time : O(n + log m),	n = size of input, m = unique x-values
        ## Space: O(m), m = number of unique x-values

        # Step 1: Group y-values by x and keep only the best one for each x
        maxYForX = defaultdict(int)  # x_val -> max y_val

        for xi, yi in zip(x, y):
            maxYForX[xi] = max(maxYForX[xi], yi)

        # Step 2: If fewer than 3 unique x-values, we can't form a valid triplet
        if len(maxYForX) < 3:
            return -1

        # Step 3: Use a max heap to get top 3 y-values
        # We use negative y-values since Python has min-heap by default
        heap = [-val for val in maxYForX.values()]
        heapq.heapify(heap)

        # Step 4: Pop top 3 values, negate them back to positives, and sum
        return -sum(heapq.heappop(heap) for _ in range(3))
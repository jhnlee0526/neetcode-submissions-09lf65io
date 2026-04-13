class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time : O(n + k log n)
        #   - O(n) to count frequencies
        #   - O(n) to build heap
        #   - O(k log n) to heappop k elements
        # Space: O(n)
        #   - O(n) for frequency map
        #   - O(n) for heap

        res = []
        numCnts = Counter(nums) # {num : cnt, ..}
        maxHeap = [(-cnt, num) for num, cnt in numCnts.items()]
        heapq.heapify(maxHeap)

        for _ in range(k):
            _, num = heapq.heappop(maxHeap)
            res.append(num)

        return res
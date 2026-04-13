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

        num_cnt = Counter(nums) # {num: cnt, ..}
        max_heap = [(-cnt, num) for num, cnt in num_cnt.items()]
        heapq.heapify(max_heap)

        for _ in range(k):
            _, num = heapq.heappop(max_heap)
            res.append(num)
        
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #{n, c}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        heap = [(-c, n) for n, c in freq.items()]
        heapq.heapify(heap)

        res = [heapq.heappop(heap)[1] for i in range(k)]
        return res
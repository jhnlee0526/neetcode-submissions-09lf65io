class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        numCnts = Counter(nums)   # {numStr : cnt, }
        maxheap = [(-cnt, numStr) for numStr, cnt in numCnts.items()]
        heapq.heapify(maxheap)

        for _ in range(k):
            _, numStr = heapq.heappop(maxheap)
            res.append(numStr)
        
        return res
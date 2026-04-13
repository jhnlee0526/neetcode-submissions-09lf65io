class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnts = Counter(nums) # {num: cnt, }
        maxHeap = [(-cnt, num) for num, cnt in cnts.items()]
        heapq.heapify(maxHeap)
        
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res
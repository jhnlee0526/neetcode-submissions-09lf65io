class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums) # {num : cnt, }
        maxheap = [(-cnt, num) for num, cnt in cnts.items()]
        heapq.heapify(maxheap)

        res = []
        for i in range(k):
            _, num = heapq.heappop(maxheap)
            res.append(num)
        
        return res
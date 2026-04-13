class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) # {num : cnt, }
        maxHeap = [(-cnt, num) for num, cnt in counts.items()]
        heapq.heapify(maxHeap) ##

        res = []
        for i in range(k):
            _, num = heapq.heappop(maxHeap)
            res.append(num)
        return res
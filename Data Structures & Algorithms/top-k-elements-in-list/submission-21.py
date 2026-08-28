class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        numCnt = Counter(nums) #{num : count, ...}
        maxHeap = [(-cnt, num) for num, cnt in numCnt.items()]
        heapq.heapify(maxHeap)

        for i in range(k):
            _, num = heapq.heappop(maxHeap)
            res.append(num)

        return res
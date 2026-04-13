class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get maxheap
        # append the top k numbers into res list upto k

        # time : log(n) - heappop()
        # space: log(n)

        numCnts = Counter(nums) # {num: cnt, }
        maxheap = [(-cnt, num) for num, cnt in numCnts.items()]
        heapq.heapify(maxheap)
        
        res = []
        for i in range(k):
            _, num = heapq.heappop(maxheap)
            res.append(num)
        
        return res
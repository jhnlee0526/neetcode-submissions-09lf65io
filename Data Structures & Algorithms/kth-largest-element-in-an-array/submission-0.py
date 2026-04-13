class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = 0

        maxheap = [-each for each in nums]
        heapq.heapify(maxheap)

        for i in range(k):
            res = heapq.heappop(maxheap)

        return -res
        

            

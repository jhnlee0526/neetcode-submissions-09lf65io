class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time : O(n + k log n)
        # space: O(n)

        res = 0

        maxheap = [-each for each in nums]
        heapq.heapify(maxheap)  # O(n)

        for i in range(k):               # O(k)
            res = heapq.heappop(maxheap) # O(log n) -> O(k log n)

        return -res
        

            

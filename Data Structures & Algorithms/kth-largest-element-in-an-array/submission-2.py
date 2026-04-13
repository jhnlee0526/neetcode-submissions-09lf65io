class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heap : Max Heap (-min heap)
        #   Time : O(n + k log n)*
        #   Sapce: O(n)
        
        res = 0
        
        numsHeap = [-num for num in nums]
        heapq.heapify(numsHeap)             # O(n) time

        for i in range(k):                  # O(k) time
            res = heapq.heappop(numsHeap)   # O(log n) time
                                            # -> O(k log n) time
        return -res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HEAP - "top k"
        #   time : O(logn)
        #   space: O(n)
        dict = {} # {num: cnt, }
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        
        heap = [(-cnt, num) for num, cnt in dict.items()]
        heapq.heapify(heap) # max heap, {(-cnt, num), }
        
        res = [heapq.heappop(heap)[1] for i in range(k)]
        return res

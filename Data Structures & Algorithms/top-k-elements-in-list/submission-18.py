class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using heap
        #   time : O(K logn)
        #   space: O(n)

        if not nums or k == 0: # edge case
            return []
        
        numMap = Counter(nums)  # {num: cnt, ..}                # O(n)
        maxHeap = [(-cnt, num) for num, cnt in numMap.items()]  # O(n) ## [(-cnt, num), ..]
        heapq.heapify(maxHeap)                                  # O(n)

        return [heapq.heappop(maxHeap)[1] for _ in range(k)]    # O(k logn)
        # topK = []
        # for i in range(k):
        #     _, num = heapq.heappop(maxHeap)                   # O(k logn)
        #     topK.append(num)
        
        # return topK
            



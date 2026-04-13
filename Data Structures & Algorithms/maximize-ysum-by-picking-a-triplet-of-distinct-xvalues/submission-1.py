class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        xyMap = {}                                  # {x_val : max y_val, }
        
        for x_, y_ in zip(x, y):                    # set up the hashmap : xyMap
            xyMap[x_] = max(xyMap.get(x_, 0), y_)
        
        # edge case
        if len(xyMap) < 3:                          # need at least 3 unique vals for a valid triplet
            return -1
        
        maxheap = [-val for val in xyMap.values()]  # (-) for the max heap
        heapq.heapify(maxheap)

        # pop the top3 vals, and bring them back to (+), and sum all.
        return -sum(heapq.heappop(maxheap) for _ in range(3))
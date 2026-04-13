class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        xyMap = {}                  # create hashmap : {x_val : max y_val, }

        for x_, y_ in zip(x, y):    # set hashmap
            xyMap[x_] = max(xyMap.get(x_, 0), y_)
        
        if len(xyMap) < 3:          # edge case: must have at least three vals for a triplet
            return -1

        maxheap = [-val for val in xyMap.values()]  # maxheap
        heapq.heapify(maxheap)

        return -sum(heapq.heappop(maxheap) for _ in range(3))
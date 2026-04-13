class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        # hashmap : {x_val : MAX y_val, }
        # if lenth of the hashmap is less than three, return -1
        # maxheap the hashmap values (Max y val)
        # return the sum of (-1) * top#3

        xyMap = {}                                  # hashmap : {x_val : MAX y_val, }
        for xVal, yVal in zip(x, y):
            xyMap[xVal] = max(xyMap.get(xVal, 0), yVal)
        
        if len(xyMap) < 3:                          # need to has at least three val in the hashmap for a triplet
            return -1

        maxheap = [-val for val in xyMap.values()]  # maxheap of hashmap values (Max y val)
        heapq.heapify(maxheap)

        return -sum(heapq.heappop(maxheap) for _ in range(3))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = Counter(nums) # {num : count, } ## using Counter(), built-in functino in python
        counts = {} ## using dictionary / hashmap
        for each in nums:
            counts[each] = counts.get(each, 0) + 1

        maxHeap = [[-cnt, num] for num, cnt in counts.items()]
        heapq.heapify(maxHeap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using Sorted()
        #   time : O(n logn)
        #   space: O(n)
        
        if not nums or k == 0:  # edge case
            return []

        numCnt = Counter(nums)                                                        # {num: cnt, ..}
        sortedNumCnt = sorted(numCnt.items(), key=lambda item: item[1], reverse=True) # [(num, cnt), ..]
        return [num for num, _ in sortedNumCnt[:k]]


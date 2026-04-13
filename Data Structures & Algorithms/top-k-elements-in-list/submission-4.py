class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #{n: c}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        cnts = [[n, c] for n, c in freq.items()]
        cnts.sort(key=lambda x: x[1], reverse=True)
        
        res = [cnts[i][0] for i in range(k)]
        return res
            
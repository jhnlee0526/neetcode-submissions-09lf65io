class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #{n : c, }
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        cnts = [[] for i in range(len(nums) + 1)] ## 
        for n, c in freq.items(): 
            cnts[c].append(n)
        
        res = []
        for i in range(len(cnts) - 1, -1, -1): ##
            for n in cnts[i]:
                if len(res) < k:
                    res.append(n)
        return res

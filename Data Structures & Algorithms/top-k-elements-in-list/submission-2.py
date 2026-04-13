class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##[WORST] sort() + 3lists: time O(n*logn), space O(n)
        # dict = {} #{num: cnt, }
        # for n in nums:
        #     dict[n] = dict.get(n, 0) + 1
        
        # freqs = [] #[[num, cnt], [1, 1], [2, 2], [3, 3]]
        # for n, c in dict.items():
        #     freqs.append([n, c])
        # freqs.sort(key=lambda x: x[1], reverse=True)
        
        # res = [] #[num, 3, 2]
        # for i in range(k):
        #     res.append(freqs[i][0])
        
        # return res


        ##[OKAY] 3lists: time O(n), space O(n)
        # dict = {} #{num: cnt, 1:1, 2:2, 3:2, }
        # for n in nums:
        #     dict[n] = dict.get(n, 0) + 1
        
        # freqs = [[] for i in range(len(nums) + 1)] #[[],[1],[2,3],[],[],[]]
        # for n, c in dict.items():
        #     freqs[c].append(n)

        # res = [] #[3, 2]
        # for i in range(len(freqs) - 1, -1, -1): # reverse order
        #     for n in freqs[i]:
        #         if len(res) >= k:
        #             break
        #         res.append(n)
        # return res


        ##[BEST] max heap: time O(k*logn), space O(n)
        dict = {} #{nums: cnts, }
        for n in nums:
            dict[n] = dict.get(n, 0) + 1
        
        heap = [(-c, n) for n, c in dict.items()]
        heapq.heapify(heap) #max heap: [(-3, 3), (-2, 2), (-1, 1)]

        res = [heapq.heappop(heap)[1] for i in range(k)]
        return res
                



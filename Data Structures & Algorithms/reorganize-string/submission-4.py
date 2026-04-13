class Solution:
    def reorganizeString(self, s: str) -> str:
        strMap = Counter(s) #{str: cnt, }
        maxHeap = [(-cnt, str) for str, cnt in strMap.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev = None # (cnt, str)

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            
            cnt, str = heapq.heappop(maxHeap)
            res += str
            cnt += 1 # decrementing cnt
            
            if prev:
                heapq.heappush(maxHeap , prev)
                prev = None
            
            if cnt < 0: # cnt still exists (greater than 0)
                prev = (cnt, str)

        return res
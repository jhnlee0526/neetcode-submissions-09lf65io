class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        
        cnts = Counter(s) # {char: cnt, }
        maxheap = [(-cnt, char) for char, cnt in cnts.items()]
        heapq.heapify(maxheap)

        prev = None # (cnt, char)
        while maxheap or prev:
            if not maxheap and prev:
                return ""
            
            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1 # decrementing

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            
            if cnt < 0: # count still exists
                prev = (cnt, char)

        return res

class Solution:
    def reorganizeString(self, s: str) -> str:
        # hashmap : {char : cnt, }
        # maxheap: {(-cnt, char), }
        # loop 

        res = ''
        
        charCnt = Counter(s)
        maxheap = [(-cnt, char) for char, cnt in charCnt.items()]
        heapq.heapify(maxheap)

        prev = None     # (cnt, char)
        while maxheap or prev:
            if not maxheap and prev:
                return ''

            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1    # decrementing

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            
            if cnt < 0: # still have some counts
                prev = (cnt, char)

        return res
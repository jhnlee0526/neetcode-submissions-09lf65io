class Solution:
    def reorganizeString(self, s: str) -> str:
        # create a hashmap: char-cnt
        # maxheap
        # while loop to get the result

        charCounts = Counter(s) # {char : cnt, }
        maxheap = [(-cnt, char) for char, cnt in charCounts.items()]
        heapq.heapify(maxheap)

        res = ""
        prev = None # (char, cnt)
        while maxheap or prev:
            if not maxheap and prev:
                return ""

            cnt, char = heapq.heappop(maxheap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            
            if cnt < 0:
                prev = (cnt, char)

        return res
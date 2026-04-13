class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s) #{char : cnt}
        maxHeap = [[-cnt, char] for char, cnt in counts.items()] #[[-cnt, char], ]
        heapq.heapify(maxHeap)

        prev = None
        res = ""

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt < 0:
                prev = [cnt, char]
            
        return res
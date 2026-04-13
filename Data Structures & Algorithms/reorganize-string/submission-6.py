class Solution:
    def reorganizeString(self, s: str) -> str:
        ### correct answer for the time complexity!

        ## [MaxHeap] using (-)*MinHeap
        #### Time: O(n log k), where n = len(s), k = number of unique characters (≤ 26)
        #### Space: O(k), for the heap and Counter

        # Step 1: Count the frequency of each character
        count = Counter(s)  # O(n) time and space

        # Step 2: Build max-heap using negative frequencies
        maxHeap = [[-cnt, char] for char, cnt in count.items()]  # O(k)
        heapq.heapify(maxHeap)  # O(k) time, not O(n log n)

        # Step 3: Initialize result and a placeholder for the previous char
        res = ""
        prev = None  # (cnt, char)

        # Step 4: Reorganize string
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""  # Cannot place the same character consecutively

            cnt, char = heapq.heappop(maxHeap)  # O(log k)
            res += char
            cnt += 1  # Used one occurrence (remember it's negative)

            if prev:
                heapq.heappush(maxHeap, prev)  # O(log k)
                prev = None

            if cnt < 0:
                prev = [cnt, char]

        return res

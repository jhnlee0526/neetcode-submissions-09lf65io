class Solution:
    def reorganizeString(self, s: str) -> str:
        ## [MaxHeap] using (-)*MinHeap
        #### Time : O(n log n) (due to heap operations).
        #### Space : O(n) (due to Counter and heap storage).

        # Step 1: Count the frequency of each character in the string
        # Example: "aabbcc" → Counter({'a': 2, 'b': 2, 'c': 2})
        count = Counter(s)  # Creates a hashmap {char: count} : Time O(n), Space O(n)

        # Step 2: Convert the frequency map into a max-heap
        # Since Python only has min-heaps, we negate the counts to simulate a max-heap
        # Example: {'a': 2, 'b': 2, 'c': 2} → maxHeap = [[-2, 'a'], [-2, 'b'], [-2, 'c']]
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)  # Convert list into a heap : Time O(n logn), Space O(n)

        # Step 3: Initialize variables
        prev = None  # Stores the previous character to avoid consecutive duplicates
        res = ""  # Stores the result string

        # Step 4: Process characters from the heap one by one
        while maxHeap or prev:  # Continue while we have characters to process : Time O(n)
            if prev and not maxHeap:  # If the previous character is left but nothing in heap, that means there was an unmatched leftover character
                return ""  # Impossible to reorganize → return empty string
            
            # Step 5: Extract the most frequent remaining character
            cnt, char = heapq.heappop(maxHeap)  # Get highest frequency character  : Time O(log n)
            res += char  # Append this character to result string
            cnt += 1  # Reduce count (since we used one instance of this character)

            # Step 6: Push the previous character back into heap if it has occurrences left
            if prev:
                heapq.heappush(maxHeap, prev)  # Reinsert previous character into heap : Time O(log n)
                prev = None  # Clear previous character

            # Step 7: Store the current character if it still has remaining occurrences
            if cnt < 0:
                prev = [cnt, char]  # Save for the next iteration
            
        # Step 8: Return the reorganized string
        return res
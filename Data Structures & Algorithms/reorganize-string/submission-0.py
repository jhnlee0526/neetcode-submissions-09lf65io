class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # Python's built-in fuction for creating a hashmap counting characters in string. {char : cnt}
        maxHeap = [[-cnt, char] for char, cnt in count.items()] # creating a list for the maxheap: adding (-) to the count so that the minheap act like a maxheap [[-cnt, char], ]
        heapq.heapify(maxHeap) # heapify the maxHeap list

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap) # pop/take out the more freq characters [cnt, char]
            res += char # append/add the most freq character to the res string
            cnt += 1 # since (-) has been added for maxheap, += 1 acts like decrementing the count of the selected character

            if prev: # if prev has a character
                heapq.heappush(maxHeap, prev) # push/add the character in the prev variable into the maxHeap list
                prev = None # clear the prev variable
            
            if cnt < 0: # since (-) has been applied... this means if the most freq character still has some counts in the maxHeap list
                prev = [cnt, char] 

        return res



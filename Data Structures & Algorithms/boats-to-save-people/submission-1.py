class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ## two pointers
        #### time : O(n logn) ~ O(n logn) + O(n)
        #### space: O(1) ~ modify the people list in-place 
        # people.sort() # time O(n logn)
        self.mergeSort(people, 0, len(people) - 1)

        count = 0
        l, r = 0, len(people) - 1
        while l <= r:  # l == r : Ensure last person is counted
            if people[l] + people[r] <= limit:
                l += 1  # Move `l` forward (see if more of lighter people can board)
            # In all cases, `r` moves (heaviest person always gets a boat)
            r -= 1  
            count += 1  # Every iteration adds 1 boat

        return count

    
    def mergeSort(self, arr: List[int], l: int, r: int) -> List[int]:
        if l >= r:
            return arr
        
        m = (l + r) // 2
        self.mergeSort(arr, l, m)
        self.mergeSort(arr, m + 1, r)
        self.merge(arr, l, m, r)


    def merge(self, arr: List[int], l: int, m: int, r: int):
        L = arr[l : m + 1]
        R = arr[m + 1 : r + 1]

        i, j = 0, 0
        k = l
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


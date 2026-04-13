class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ## two pointers
        #### time : O(n logn) ~ O(n logn) + O(n)
        #### space: O(1) ~ modify the people list in-place 
        people.sort() # time O(n logn)

        count = 0
        l, r = 0, len(people) - 1
        while l <= r:  # l == r : Ensure last person is counted
            if people[l] + people[r] <= limit:
                l += 1  # Move `l` forward (see if more of lighter people can board)
            # In all cases, `r` moves (heaviest person always gets a boat)
            r -= 1  
            count += 1  # Every iteration adds 1 boat

        return count
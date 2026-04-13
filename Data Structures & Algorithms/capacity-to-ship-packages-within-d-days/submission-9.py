class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search
        #   time : O(n log s), n - length of weights, s - sum of weights
        #   space: O(1)

        l, r = max(weights), sum(weights) ##  # on list 'capacity'
        while l <= r:
            mWeight = l + (r - l) // 2

            spentDays = 1   ##
            weightSum = 0   ##
            for curWeight in weights:
                if curWeight + weightSum > mWeight: # If I try to add this package to today's ship and it exceeds the limit, I must wait and load it tomorrow.
                    spentDays += 1
                    weightSum = 0
                weightSum += curWeight
            
            if spentDays <= days:   # If current capacity works within the day limit,
                r = mWeight - 1          # try smaller capacity (for the least weight capacity)
            else:                   # If too many days
                l = mWeight + 1         # increase capacity
        
        return l


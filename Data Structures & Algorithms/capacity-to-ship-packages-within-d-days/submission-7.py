class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search
        #   time : O(n logS) - n = length of weights, S = sum of weights
        #   space: O(1)

        l, r = max(weights), sum(weights)

        while l <= r:
            midW = l + (r - l) // 2

            usedDays = 1
            curW = 0
            for eachW in weights:
                # If I try to add this package to today's ship and it exceeds the limit, I must wait and load it tomorrow.
                if curW + eachW > midW:
                    usedDays += 1
                    curW = 0
                curW += eachW
            
            if usedDays <= days:
                r = midW - 1
            else:
                l = midW + 1
        
        return l
                
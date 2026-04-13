class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            m = (l + r) // 2

            totalWeight = 0
            reqDays = 1

            for curWeight in weights:
                if curWeight + totalWeight > m:
                    reqDays += 1
                    totalWeight = 0
                totalWeight += curWeight
            
            if reqDays > days:
                l = m + 1
            else:
                res = m
                r = m - 1

        return res
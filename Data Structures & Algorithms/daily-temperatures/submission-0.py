class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force
        #   time : O(n^2)
        #   space: O(n)
        res = []
        for i in range(len(temperatures)):
            curTemp = temperatures[i]
            foudWarmerDay = False
            for j in range(i + 1, len(temperatures)):
                nextTemp = temperatures[j]

                if curTemp < nextTemp:
                    res.append(j - i)
                    foudWarmerDay = True
                    break

            if not foudWarmerDay:
                res.append(0)
        return res
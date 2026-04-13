class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Stack
        #   time : O(n)
        #   space: O(n)
        
        res = [0] * len(temperatures)
        stack = []  # [[temp, idx], ...]

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while (
                stack and
                stack[-1][0] < temp
            ):
                sTemp, sIdx = stack.pop()
                res[sIdx] = i - sIdx

            stack.append([temp, i])
        
        return res

        #----------------
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
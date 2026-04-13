class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS with queue 'iteratively'
        if amount == 0:
            return 0

        def bfs(): # iteratively
            queue = deque()
            queue.append((0, 0)) # [(sum, cnt), ]
            
            visits = set() # prevent cycling: {sum, }

            while queue:
                sum, cnt = queue.popleft()
                for coin in coins:
                    nextSum = coin + sum
                    
                    if nextSum == amount:
                        return cnt + 1
                    
                    if (
                        nextSum > 0 and
                        nextSum < amount and
                        nextSum not in visits
                    ):
                        visits.add(nextSum)
                        queue.append((nextSum, cnt + 1))
            return -1

        return bfs()


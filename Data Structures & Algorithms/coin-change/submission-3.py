class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS iteratively wih queue + 'visits' set()
        # Time:  O(amount × len(coins)) — worst case visits many sums
        # Space: O(amount) — stores up to `amount` visited states
        
        if amount == 0: # edge case
            return 0

        # setting up queue
        queue = deque() # [(sum, cnt), ]
        queue.append((0, 0))

        visits = set() # {sum, } - preventing cycle
        
        while queue:
            sum, cnt = queue.popleft()
            
            for coin in coins:
                nextSum = sum + coin
                
                if nextSum == amount:
                    return cnt + 1 # Found exact match!
                
                if (
                    0 < nextSum < amount and
                    nextSum not in visits
                ):
                    queue.append((nextSum, cnt + 1))
                    visits.add(nextSum)
        
        return -1



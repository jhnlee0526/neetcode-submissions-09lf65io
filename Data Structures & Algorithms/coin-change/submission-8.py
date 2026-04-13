class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bfs iteratively with queue (sum, cnt) + hashset(visits) preventing cycling
        ## Time:  O(amount × len(coins)) — worst case visits many sums
        ## Space: O(amount) — stores up to `amount` visited states

        if amount == 0:
            return 0

        # set up visits & queue
        visits = set()      # prevent cylcing, {sum, ...}##
        queue = deque()     # [(sum, cnt), ...]
        queue.append((0, 0))

        while queue:
            curSum, cnt = queue.popleft()
            
            for curCoin in coins:
                nextSum = curCoin + curSum

                if nextSum == amount:   # found it!
                    return cnt + 1
                
                if (
                    0 < nextSum < amount and 
                    nextSum not in visits
                ):
                    visits.add(nextSum) ##
                    queue.append((nextSum, cnt + 1))
            
        return -1
        
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bfs iteratively with queue((curSum, cnt)) + visits(hashset)

        if amount == 0:
            return 0

        queue = deque()         # [(curSum, cnt), ...]
        queue.append((0, 0))
        visits = set()          # {curSum, ...}, preventing cycle

        while queue:
            curSum, cnt = queue.popleft()
            for curCoin in coins:
                nextSum = curSum + curCoin
                
                if nextSum == amount:
                    return cnt + 1
                
                if (
                    0 < nextSum < amount and
                    nextSum not in visits
                ):
                    queue.append((nextSum, cnt + 1))
                    visits.add(nextSum)

        return -1



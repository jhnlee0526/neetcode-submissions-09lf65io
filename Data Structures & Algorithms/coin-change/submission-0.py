class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BFS with queue 'iteratively': explore the fewest coins needed to reach the amount
        ## Time: O(n * t), where n = number of coins, t = amount
        ## Space: O(t), for visited set and queue

        if amount == 0:  # Edge case: 0 coins needed to make amount 0
            return 0

        q = deque()
        q.append((0, 0))  # Each element is (current_sum, number_of_coins_used)
        visited = set()   # To prevent revisiting the same sum

        while q:
            curr_sum, num_coins = q.popleft()

            for coin in coins:
                next_sum = curr_sum + coin

                if next_sum == amount:
                    return num_coins + 1  # Found the solution: add one coin

                # if 0 < next_sum < amount and next_sum not in visited:
                if (
                    next_sum > 0 and 
                    next_sum < amount and 
                    next_sum not in visited
                ):
                    visited.add(next_sum)
                    q.append((next_sum, num_coins + 1))

        return -1  # If no combination can make up the amount
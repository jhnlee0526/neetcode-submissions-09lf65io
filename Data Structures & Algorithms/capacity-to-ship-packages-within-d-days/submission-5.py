class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search on capacity K
        # time:  O(n · log S), where n = len(weights), S = sum(weights)
        # space: O(1)

        left, right = max(weights), sum(weights)

        while left <= right:
            mid = (left + right) // 2

            days_used, curr = 1, 0
            for w in weights:
                if curr + w > mid:
                    days_used += 1
                    curr = 0
                curr += w

            if days_used <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left
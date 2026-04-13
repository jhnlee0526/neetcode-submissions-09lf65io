class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # [Binary Search] to find minimum ship capacity
        ## Time:  O(n log m), where:
        '''
            n = number of packages (len(weights))
            m = range of ship capacities from max(weights) to sum(weights)
                → total guesses ≈ log(sum - max)
        '''
        ## Space: O(1)

        # Left boundary: cannot be less than the heaviest package
        left = max(weights)

        # Right boundary: max capacity = all packages in one shipment
        right = sum(weights)

        result = right  # Start with upper bound as fallback

        # Binary search for the smallest valid ship capacity
        while left <= right:
            mid = (left + right) // 2  # Try mid as the ship's capacity
            currentWeight = 0
            requiredDays = 1  # Start with day 1

            # Simulate shipping based on current capacity
            for weight in weights:
                # If I try to add this package to today's ship and it exceeds the limit, I must wait and load it tomorrow.
                if currentWeight + weight > mid:
                    requiredDays += 1
                    currentWeight = 0   # Start a new shipment (new day)
                currentWeight += weight # still load the current weight, since every package must be shipped in order.

            # If current capacity works within the day limit, try smaller capacity
            if requiredDays <= days:
                result = mid
                right = mid - 1
            else:
                left = mid + 1  # Too many days → increase capacity

        return result

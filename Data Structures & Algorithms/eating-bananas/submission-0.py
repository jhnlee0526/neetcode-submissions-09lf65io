class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## [Binary Search]
        #### time : O(n × log m)
        # - n = number of piles
        # - m = max(piles), which is the largest possible eating speed
        # → For each speed guess (log m), you check all piles (O(n))
        #### space: O(1)
        # - No extra memory beyond a few variables for the search bounds and hour count


        # We are trying to find the minimum eating speed `k`
        # such that Koko can finish all bananas in `h` hours

        l = 1                    # Lower bound for k (minimum possible speed)
        r = max(piles)          # Upper bound for k (if she eats the biggest pile in 1 hour)
        minPiles = r            # Initialize result with the upper bound

        # Binary search to find the minimum valid eating speed
        while l <= r:
            k = (l + r) // 2    # Try a middle speed k
            totalHours = 0      # Track how many hours it takes with this speed

            # For each pile, calculate the time to eat with speed k
            for pile in piles:
                totalHours += math.ceil(pile / k)  # Round up since partial piles take a whole hour

            # If we can finish in h hours or less, try a slower speed
            if totalHours <= h:
                minPiles = min(minPiles, k)  # Update minimum valid speed found
                r = k - 1  # Try smaller k
            else:
                l = k + 1  # Try larger k to speed up eating

        return minPiles  # Return the smallest k that lets Koko finish on time


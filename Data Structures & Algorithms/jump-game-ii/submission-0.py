class Solution:
    def jump(self, nums: List[int]) -> int:
        # [Greedy BFS] "iteratively"
        # Time: O(n) — we only scan each element once
        # Space: O(1) — just using counters and pointers

        res = 0   # This counts how many jumps we've made so far
        l = 0     # Left pointer: start of the current "jump window"
        r = 0     # Right pointer: end of the current "jump window"

        while r < len(nums) - 1:
            # While we haven’t yet reached the end of the list...

            farthest = 0  # This will track the farthest we can reach in the next jump

            # Explore every index we can jump to from the current window [l, r]
            for i in range(l, r + 1):
                # From position i, how far can we jump?
                # i + nums[i] = reach from current position
                farthest = max(farthest, i + nums[i])

            # After checking all positions in the current window:
            # Update our jump window to [r+1, farthest]
            l = r + 1
            r = farthest

            res += 1  # We’ve made one jump

        return res  # Return how many jumps we used to reach the end

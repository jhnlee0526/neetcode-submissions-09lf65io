class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy BFS, iteratively
        ## Time: O(n) — we only scan each element once
        ## Space: O(1) — just using counters and pointers
        
        def bfs():
            jumps = 0      # Count of jumps made
            l = r = 0      # Current window: all indices we can reach in this jump

            while r < len(nums) - 1:
                farthest = 0
                for i in range(l, r + 1):  # Explore all indices in current level
                    farthest = max(farthest, i + nums[i])
                l = r + 1       # Shift window start to just beyond current reach
                r = farthest    # Extend window end to the farthest reachable index
                jumps += 1      # One jump gets us into this next window

            return jumps

        return bfs()
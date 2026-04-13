class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs recursively
        #   Time : O(R × C) — each cell visited once
        #   Space: O(R × C) — visited set + recursion stack in worst case

        # edge case
        if not grid or not grid[0]:
            return 0

        maxArea = 0
        
        RC, CC = len(grid), len(grid[0])
        visits = set()  # {(r, c), ..}
        
        def dfs(r, c): # recursively
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                grid[r][c] == 0
            ):
                return 0
            
            visits.add((r, c))

            curArea = 1 ##
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    (nextR, nextC) not in visits and
                    grid[nextR][nextC] == 1
                ):
                    curArea += dfs(nextR, nextC)    ##
                
            return curArea


        for r in range(RC):
            for c in range(CC):
                if (
                    r in range(RC) and
                    c in range(CC) and
                    (r, c) not in visits and
                    grid[r][c] == 1
                ):  
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # dfs recursively
        #   time : O(r * c), visits each cells once at most
        #   space: O(r * c), recursive stack

        # edge case
        if not grid or not grid[0]:
            return
        
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, dist):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] < dist   # already shorter dist.
            ):
                return
            
            grid[r][c] = dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, dist + 1)

        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
                    
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # dfs recursively
        #   time :
        #   space:

        # edge case
        if not grid or not grid[0]:
            return
        
        RC, CC = len(grid), len(grid[0])

        def dfs(r, c, dist): # recursively
            # base case : 
            #   stop if 1) out of bounds or 
            #   if 2) this cell already has a shorter distance
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] < dist
            ):
                return
            
            grid[r][c] = dist

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                dfs(nextR, nextC, dist + 1)

        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0:         # starting from the treasure
                    dfs(r, c, 0)

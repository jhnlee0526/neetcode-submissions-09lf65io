class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # dfs(from multiple-source) recursively
        #   time : O(R * C), Each cell is updated at most once.
        #   space: O(R * C), recursion stack in the worst case

        if not grid or not grid[0]:     # edge case
            return
        
        RC, CC = len(grid), len(grid[0])

        def dfs(r, c, distance):        # recursively
            # base case : stop if 1) out of bounds or if 2) this cell already has a shorter distance
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] < distance
            ):
                return
            
            # update the cell with the new shortest distance
            grid[r][c] = distance
            
            # recursively traversing neighbors
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                dfs(nextR, nextC, distance + 1)
        
        # start dfs() from every treasure cells
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
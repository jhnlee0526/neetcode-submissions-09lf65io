class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        visits = set() # (r, c)
        cnt = 0
        RC = len(grid)
        CC = len(grid[0])

        def dfs(r, c): # recursively
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] == "0" or
                (r, c) in visits
            ):
                return
            
            visits.add((r, c)) #

            # move to each directions and run dfs()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # init dfs
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == "1"
                ):
                    cnt += 1
                    dfs(r, c)
        
        return cnt
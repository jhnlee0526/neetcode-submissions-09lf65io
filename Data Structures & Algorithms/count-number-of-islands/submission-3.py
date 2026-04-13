class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        cnt = 0
        visits = set()
        rc, cc = len(grid), len(grid[0])

        def dfs(r, c):
            # base case
            if (
                r not in range(rc) or
                c not in range(cc) or
                grid[r][c] == "0" or
                (r, c) in visits
            ):
                return

            visits.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        
        for r in range(rc):
            for c in range(cc):
                if (r, c) not in visits and grid[r][c] == "1":
                    cnt += 1
                    dfs(r, c)        

        return cnt
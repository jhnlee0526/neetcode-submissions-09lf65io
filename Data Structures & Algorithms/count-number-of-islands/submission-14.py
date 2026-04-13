class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs recursively with hashset for visits
        
        # edge case
        if not grid or not grid[0]: ##
            return 0
        
        res = 0

        visits = set()  # (r, c)
        RC, CC = len(grid), len(grid[0])

        def dfs(r, c):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] == '0' or
                (r, c) in visits
            ):
                return
            
            visits.add((r, c)) ##

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if (
                    newR in range(RC) and
                    newC in range(CC) and
                    grid[newR][newC] == '1' and
                    (newR, newC) not in visits
                ):
                    dfs(newR, newC)

        for r in range(RC):
            for c in range(CC):
                if (
                    grid[r][c] == '1' and
                    (r, c) not in visits
                ):
                    res += 1
                    dfs(r, c)
        
        return res
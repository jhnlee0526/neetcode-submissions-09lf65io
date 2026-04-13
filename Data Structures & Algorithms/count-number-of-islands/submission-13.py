class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use hashset for visits: (r,c)
        # dfs() recursively to find the # of islands

        # edge case
        if not grid or not grid[0]:
            return 0
        
        cnt = 0
        visits = set() # {(r, c), }
        RC, CC = len(grid), len(grid[0])

        def dfs(r, c): # recursively
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                grid[r][c] == '0'
            ): 
                return
            
            visits.add((r, c))
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    grid[nextR][nextC] == '1' and
                    (nextR, nextC) not in visits
                ):
                    dfs(nextR, nextC)


        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == '1'
                ):
                    cnt += 1
                    dfs(r, c)

        return cnt

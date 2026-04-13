class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        cnt = 0
        visits = set()
        rowCnt = len(grid)
        colCnt = len(grid[0])

        def dfs(r, c):
            # base case
            if (
                r not in range(rowCnt) or
                c not in range(colCnt) or
                grid[r][c] == "0" or
                (r, c) in visits
            ):
                return
            
            visits.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        

        for row in range(rowCnt):
            for col in range(colCnt):
                if (row, col) not in visits and grid[row][col] == "1":
                    cnt += 1
                    dfs(row, col)
        return cnt
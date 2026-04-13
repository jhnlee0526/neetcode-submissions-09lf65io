class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        resCnt = 0
        visits = set() # {(r, c), }
        RC = len(grid) 
        CC = len(grid[0])

        ## Breadth First Search
        def bfs(r, c): # iteratively with queue
            q = deque()
            q.append((r,c))
            visits.add((r,c))

            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = r + dr, c + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        grid[nextR][nextC] == '1' and
                        (nextR, nextC) not in visits
                    ):
                        visits.add((nextR, nextC))
                        q.append((nextR, nextC))

        # ## Depth First Search
        # def dfs(r, c): # recursively
        #     # base case
        #     if (
        #         r not in range(RC) or
        #         c not in range(CC) or
        #         (r, c) in visits or
        #         grid[r][c] == '0'
        #     ):
        #         return
            
        #     visits.add((r, c))
            
        #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #     for dr, dc in directions:
        #         nextR, nextC = r + dr, c + dc
        #         if (
        #             nextR in range(RC) or
        #             nextC in range(CC) or
        #             (nextR, nextC) not in visits or
        #             grid[nextR][nextC] == '1'
        #         ):
        #             dfs(nextR, nextC)


        ## init bfs / dfs
        for r in range(RC):
            for c in range(CC):
                if (r, c) not in visits and grid[r][c] == '1':
                    # dfs(r, c)
                    bfs(r, c)
                    resCnt += 1
            
        return resCnt

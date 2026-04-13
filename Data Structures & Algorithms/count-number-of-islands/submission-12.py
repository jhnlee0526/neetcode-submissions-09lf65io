class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use hashset for visits
        # bfs() with queue to find # of island

        # edge case
        if not grid or not grid[0]:
            return 0

        res = 0
        visits = set() # {(r, c), }
        RC, CC = len(grid), len(grid[0])
        
        def bfs(r, c): # iteratively with queue
            queue = deque()
            queue.append((r, c))
            visits.add((r, c))

            while queue:
                qr, qc = queue.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        grid[nextR][nextC] == '1' and
                        (nextR, nextC) not in visits
                    ):
                        visits.add((nextR, nextC))
                        queue.append((nextR, nextC))


        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == '1'
                ): 
                    res += 1
                    bfs(r, c)
        
        return res

        
        
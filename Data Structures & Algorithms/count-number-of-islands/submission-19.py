class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs iteratively with queue + hashset for visits
        cnts = 0
        
        visits = set() # {(r, c),}
        RC, CC = len(grid), len(grid[0])

        def bfs(r, c):  # iteratively with queue
            q = deque()
            q.append((r, c))    # queue
            visits.add((r, c))  # visits

            while q:
                qr, qc = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        (nextR, nextC) not in visits and
                        grid[nextR][nextC] == '1'
                    ):
                        q.append((nextR, nextC))    # queue
                        visits.add((nextR, nextC))  # visits

        
        # initial invokation of bfs()
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == '1'
                ):
                    cnts += 1
                    bfs(r, c)
        
        return cnts

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs iteratively with queue, with hashset(visits)
        cnts = 0
        
        visits = set()  # {(r, c), }
        RC, CC = len(grid), len(grid[0])

        def bfs(r, c):  # iteratively
            visits.add((r, c))

            queue = deque()
            queue.append((r, c))
            
            while queue:
                qr, qc = queue.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = dr + qr, dc + qc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        (nextR, nextC) not in visits and
                        grid[nextR][nextC] == '1'
                    ):
                        visits.add((nextR, nextC))
                        queue.append((nextR, nextC))
                        

        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == '1'
                ):
                    cnts += 1
                    bfs(r, c)

        return cnts
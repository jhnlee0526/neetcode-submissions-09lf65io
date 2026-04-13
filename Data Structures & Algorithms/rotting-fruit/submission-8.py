class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs iteratively with queue for rotten ones
        time = 0
        fresh = 0

        RC, CC = len(grid), len(grid[0])

        # set up the count for fresh fruits AND the queue for rotten ones
        rottQ = deque()
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rottQ.append((r, c))
        
        # bfs iteratively with queue
        while rottQ and fresh:
            for i in range(len(rottQ)):
                qr, qc = rottQ.popleft()
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        grid[nextR][nextC] == 1
                    ):
                        grid[nextR][nextC] = 2
                        rottQ.append((nextR, nextC))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1


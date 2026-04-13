class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs with queue (iteratively)
        rottQ = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rottQ.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh and rottQ:
            for i in range(len(rottQ)):
                qr, qc = rottQ.popleft()
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(len(grid)) and
                        nextC in range(len(grid[0])) and
                        grid[nextR][nextC] == 1
                    ):
                        grid[nextR][nextC] = 2
                        fresh -= 1
                        rottQ.append((nextR, nextC))
            time += 1

        return time if fresh == 0 else -1

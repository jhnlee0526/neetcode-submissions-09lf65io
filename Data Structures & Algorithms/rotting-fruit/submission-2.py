class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottQueue = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rottQueue.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh and rottQueue:
            for i in range(len(rottQueue)):
                qr, qc = rottQueue.popleft()

                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(len(grid)) and
                        nextC in range(len(grid[0])) and
                        grid[nextR][nextC] == 1
                    ):
                        grid[nextR][nextC] = 2
                        fresh -= 1
                        rottQueue.append((nextR, nextC))

            time += 1

        return time if fresh == 0 else -1
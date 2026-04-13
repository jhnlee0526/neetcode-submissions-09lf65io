class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs iteratively with queue(rotten)
        time = 0

        RC, CC = len(grid), len(grid[0])

        # set fresh & rotQ
        fresh = 0
        rotQ = deque() # [(r, c), ]
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotQ.append((r, c))
        
        # bfs iteratively
        while rotQ and fresh:
            for _ in range(len(rotQ)):
                qr, qc = rotQ.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = dr + qr, dc + qc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        grid[nextR][nextC] == 1
                    ):
                        grid[nextR][nextC] = 2
                        fresh -= 1
                        rotQ.append((nextR, nextC))

            time += 1
        

        return time if fresh == 0 else -1

        
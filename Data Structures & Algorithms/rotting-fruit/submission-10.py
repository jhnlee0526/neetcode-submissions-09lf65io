class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs iteratively with queue for rotten + fresh cnts
        #  time :
        #  space:
        
        # edge case
        if not grid or not grid[0]:
            return -1

        resTime = 0

        RC, CC = len(grid), len(grid[0])
        fresh = 0
        rottQ = deque()
        
        # set the fresh and rottQ
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rottQ.append((r, c))

        # bfs traversal
        while rottQ and fresh:
            for _ in range(len(rottQ)):
                qr, qc = rottQ.popleft()
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        (nextR, nextC) not in rottQ and
                        grid[nextR][nextC] == 1
                    ):
                        grid[nextR][nextC] = 2
                        fresh -= 1
                        rottQ.append((nextR, nextC))
            
            resTime += 1
        
        return resTime if fresh == 0 else -1

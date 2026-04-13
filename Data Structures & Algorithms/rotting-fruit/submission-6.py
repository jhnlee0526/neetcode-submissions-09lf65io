class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        
        RC, CC = len(grid), len(grid[0])
        
        # set up the queue
        rottQ = deque()
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rottQ.append((r, c))
        
        # bfs with queue
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while rottQ and fresh:
            for i in range(len(rottQ)):
                r, c = rottQ.popleft()    
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if (
                        newR in range(RC) and
                        newC in range(CC) and
                        grid[newR][newC] == 1
                    ):
                        grid[newR][newC] = 2
                        fresh -= 1
                        rottQ.append((newR, newC))
            time += 1
        
        return time if fresh == 0 else -1
            
        
                    
        

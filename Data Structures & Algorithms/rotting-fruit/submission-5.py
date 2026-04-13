class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ## BFS with queue
        
        rottQ = deque()
        fresh = 0
        time = 0

        RC, CC = len(grid), len(grid[0])
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rottQ.append((r, c))
                
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh and rottQ:
            for i in range(len(rottQ)):
                r, c = rottQ.popleft()
                for dr, dc in directions:
                    if (
                        r + dr in range(RC) and
                        c + dc in range(CC) and
                        grid[r + dr][c + dc] == 1
                    ):
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
                        rottQ.append((r + dr, c + dc))     
            time += 1

        return time if fresh == 0 else -1
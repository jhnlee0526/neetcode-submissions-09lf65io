class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs iteratively with queue, with hashset for visits
        if not grid or not grid[0]: # edge case 
            return 0
        
        res = 0
        
        visits = set()  # {(r, c), }
        RC, CC = len(grid), len(grid[0])
        
        def bfs(r, c):
            visits.add((r, c))
            
            queue = deque()
            queue.append((r, c))

            while queue:
                qr, qc = queue.popleft()
            
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    newR, newC = dr + qr, dc + qc
                    if (
                        newR in range(RC) and
                        newC in range(CC) and
                        grid[newR][newC] == '1' and
                        (newR, newC) not in visits
                    ):
                        visits.add((newR, newC))
                        queue.append((newR, newC))
                        
        
        for r in range(RC):
            for c in range(CC):
                if (
                    grid[r][c] == '1' and
                    (r, c) not in visits
                ):
                    res += 1
                    bfs(r, c)

        return res
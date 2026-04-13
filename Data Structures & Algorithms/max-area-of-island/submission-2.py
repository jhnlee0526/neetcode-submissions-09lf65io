class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # bfs iteratively
        #   time : O(RC)
        #   space: O(RC)

        if not grid or not grid[0]:
            return 0
        
        maxArea = 0
        
        RC, CC = len(grid), len(grid[0])
        visits = set() # {(r, c), ..}
        q = deque()    # [(r, c), ..]

        def bfs(r, c): # iteratively
            q.append((r, c))
            visits.add((r, c))

            curArea = 0
            while q:
                curArea += 1
                qr, qc = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        (nextR, nextC) not in visits and
                        grid[nextR][nextC] == 1
                    ):
                        visits.add((nextR, nextC))
                        q.append((nextR, nextC))
                
            return curArea

        
        for r in range(RC):
            for c in range(CC):
                if (
                    r in range(RC) and
                    c in range(CC) and
                    (r, c) not in visits and
                    grid[r][c] == 1
                ):
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea
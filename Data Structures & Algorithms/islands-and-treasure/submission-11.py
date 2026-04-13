class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs iteratively + queue
        #   time : O(R*C)
        #   space: O(R*C)

        if not grid or not grid[0]:
            return
        
        RC, CC = len(grid), len(grid[0])
        q = deque() # [(r, c, dist), ..]

        # deque the treasure points
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0: # treasure point
                    q.append((r, c, 0))

        # BFS from all treasures
        while q:
            qr, qc, qd = q.popleft()

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC, nextD = qr + dr, qc + dc, qd + 1
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    grid[nextR][nextC] == 2147483647  # only update empty rooms
                ):
                    grid[nextR][nextC] = nextD
                    q.append((nextR, nextC, nextD))

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        cnt = 0
        visits = set()
        RC, CC = len(grid), len(grid[0])

        def bfs(r, c): #with queue, iteratively
            queue = deque()
            queue.append((r, c))
            visits.add((r, c))

            while len(queue) > 0:
                qr, qc = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    if (
                        qr + dr in range(RC) and
                        qc + dc in range(CC) and
                        (qr + dr, qc + dc) not in visits and
                        grid[qr + dr][qc + dc] == "1"
                    ):
                        queue.append((qr + dr, qc + dc))
                        visits.add((qr + dr, qc + dc))


        for r in range(RC):
            for c in range(CC):
                if (r, c) not in visits and grid[r][c] == "1":
                    cnt += 1
                    bfs(r, c)

        return cnt
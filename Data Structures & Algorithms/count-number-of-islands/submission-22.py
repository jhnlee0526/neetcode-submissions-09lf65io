class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs iteratively
        #   time : O(r * c) 
        #   space: O(r * c)

        # edge case
        if not grid or not grid[0]:
            return 0

        cnt = 0

        RC, CC = len(grid), len(grid[0])
        visits = set()                      # {(r, c), ...}
        q = deque()                         # [(r, c), ...]

        def bfs(r, c): #recursively
            nonlocal cnt

            visits.add((r, c))
            q.append((r, c))
            
            while q:
                qr, qc = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        (nextR, nextC) not in visits and
                        grid[nextR][nextC] == '1'
                    ):
                        visits.add((nextR, nextC))
                        q.append((nextR, nextC))

        for r in range(RC):
            for c in range(CC):
                if (
                    r in range(RC) and
                    c in range(CC) and
                    (r, c) not in visits and
                    grid[r][c] == '1'
                ):
                    cnt += 1
                    bfs(r, c)

        return cnt
                

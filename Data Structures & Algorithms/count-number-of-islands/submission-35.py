class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS iteratively with queue +  hashmap for visiting
        #   time : O(r * c) - visiting each cells once at most
        #   space: O(r * c) - hashmap for visiting + queue

        # edge case
        if not grid or not grid[0]:
            return 0

        count = 0
        visits = set()  # {(r, c), ...}

        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque([(r, c)]) # [(r, c), ...]
            
            while q:
                qr, qc = q.popleft()
                visits.add((qr, qc))

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if (
                        nr in range(RC) and
                        nc in range(CC) and
                        (nr, nc) not in visits and
                        grid[nr][nc] == "1"
                    ):
                        q.append((nr, nc))

        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == "1"
                ):
                    bfs(r, c)
                    count +=1

        return count
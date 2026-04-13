class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs iteratively with queue "Multi-source"(start from all treasure cells at once)
        #   time : O(r * c), each cell is processed at most once
        #   space: O(r * c), queue in worst case

        # edge case
        if not grid or not grid[0]:
            return
        
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        # 🔹 Step 1: Initialize queue with ALL treasure cells (value == 0)
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0:
                    q.append((r, c))
        # 🔹 Step 2: BFS
        while q:
            qr, qc = q.popleft()
            for dr, dc in directions:
                nr, nc = qr + dr, qc + dc
                # edge case
                if (
                    nr in range(RC) and
                    nc in range(CC) and
                    grid[nr][nc] == 2147483647   # can be traversed
                ):
                    grid[nr][nc] = grid[qr][qc] + 1   # Update distance
                    q.append((nr, nc))


        # -------------------
        # dfs recursively (from the treasure chest)
        #   time : O(r * c), visits each cells once at most
        #   space: O(r * c), recursive stack

        # edge case
        if not grid or not grid[0]:
            return
        
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, dist):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] < dist   # already shorter dist.
            ):
                return
            
            grid[r][c] = dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, dist + 1)

        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0:
                    dfs(r, c, 0)

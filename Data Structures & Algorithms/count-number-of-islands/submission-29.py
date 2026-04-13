class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS iteratively w/ queue + hashset for visits
        #   Time : O(r * c)
        #   Space: O(r * c)
        
        # edge case
        if not grid or not grid[0]:
            return 0
        
        counts = 0
        visits = set()  # {(r, c), ..}
        q = deque()     # [(r, c), ..]

        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(r, c):
            q.append((r, c))
            visits.add((r, c))
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if (
                        nr in range(RC) and
                        nc in range(CC) and
                        grid[nr][nc] == '1' and
                        (nr, nc) not in visits
                    ):
                        q.append((nr, nc))
                        visits.add((nr, nc))

        for r in range(RC):
            for c in range(CC):
                if (
                    grid[r][c] == '1' and
                    (r, c) not in visits
                ):
                    counts += 1
                    bfs(r, c)
        
        return counts

        ##############################
        # DFS recursively + hashset for visits
        #   Time : O(r * c)
        #   Space: O(r * c) for visited set and recursion stack

        counts = 0
        visits = set()  # {(r, c), ..}
        
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] == '0' or
                (r, c) in visits
            ):
                return
            
            visits.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc) 
   
        for r in range(RC):
            for c in range(CC):
                if (
                    grid[r][c] == '1' and
                    (r, c) not in visits
                ):
                    counts += 1
                    dfs(r, c)

        return counts

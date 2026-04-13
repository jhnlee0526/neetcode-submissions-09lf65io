class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS iteratively w/ queue + hashset for visits
        #   Time : O(r * c), Each cell is visited once at most
        #   Space: O(r * c), HashSet for visited cells + queue in worst case

        # edge case
        if not grid or not grid[0]:
            return 0
        
        cnts = 0
        visits = set()  # {(r, c), ..}
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque([(r, c)])     # [(r, c), ..]
            while q:
                qr, qc = q.popleft()
                visits.add((qr, qc))

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if (
                        nr in range(RC) and
                        nc in range(CC) and
                        (nr, nc) not in visits and
                        grid[nr][nc] == '1'
                    ):
                        q.append((nr, nc))
        
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == '1'
                ):
                    cnts += 1
                    bfs(r, c)
        
        return cnts

        
        # DFS recursively + hashmap for visits
        #   Time : O(r * c)
        #   Space: O(r * c) for visited set and recursion stack

        cnts = 0
        visits = set()  # {(r, c), ..}
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                grid[r][c] == '0'
            ):
                return
            
            visits.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == '1'
                ):
                    cnts += 1
                    dfs(r, c)
            
        return cnts
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Graph: BFS iteratively w/ queue + hashset for visits
        #   time : O(R * C), visits each cell once at most
        #   space: O(R * C), BFS queue & visits hashseet

        counts = 0
        visits = set()  # {(r, c), ..}

        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque() # [(r, c), ..]

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
                        (nr, nc) not in visits and
                        grid[nr][nc] == "1"
                    ):
                        q.append((nr, nc))
                        visits.add((nr, nc))

        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == "1"
                ):
                    bfs(r, c)
                    counts += 1

        return counts


        #----------------
        # Graph : DFS recursively + hashset for visits
        #   time : O(R * C), visits each cells once at most
        #   space: O(R * C), recursive stack & visits hashset

        counts = 0
        visits = set()  # {(r, c), ..}

        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                grid[r][c] == "0" 
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
                    grid[r][c] == "1"
                ):
                    dfs(r, c)
                    counts += 1

        return counts

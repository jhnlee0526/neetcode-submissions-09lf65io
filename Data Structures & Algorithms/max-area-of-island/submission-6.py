class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # bfs iteratively with queue + hashmap for visits
        #   time :
        #   space:

        # edge case 
        if not grid or not grid[0]:
            return 0
        
        maxArea = 0
        visits = set()  # {(r, c), ..}
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()     # [(r, c), ..]

        def bfs(r, c):
            # edge case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                grid[r][c] == 0
            ):
                return 0

            q.append((r, c))   
            visits.add((r, c))
            curArea = 0

            while q:
                qr, qc = q.popleft()
                curArea += 1

                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if (
                        nr in range(RC) and
                        nc in range(CC) and
                        (nr, nc) not in visits and
                        grid[nr][nc] == 1
                    ):
                        visits.add((nr, nc))
                        q.append((nr, nc))

            return curArea
        

        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == 1
                ):
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea

        # --------------
        # dfs recursively + hashmap for visits
        #   time : O(r * c), visits every cells once at most
        #   space: O(r * c), hashmap for visits & recursive stack

        # edge case
        if not grid or not grid[0]:
            return 0

        maxArea = 0
        visits = set()  # {(r, c), ..}
        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                grid[r][c] == 0
            ):
                return 0

            visits.add((r, c))
            curArea = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                curArea += dfs(nr, nc)

            return curArea


        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == 1
                ):
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
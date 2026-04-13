class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # ✅ DFS recursively
        #   Time : O(R × C) — each cell visited once
        #   Space: O(R × C) — recursion stack + visited set

        count = 0

        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        visits = set()

        def dfs(r, c):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] != '1' or
                (r, c) in visits
            ):
                return
            
            visits.add((r, c))

            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    grid[nextR][nextC] == '1' and
                    (nextR, nextC) not in visits
                ):
                    dfs(nextR, nextC)

        for r in range(RC):
            for c in range(CC):
                if (
                    grid[r][c] == '1' and
                    (r, c) not in visits
                ):
                    # Start DFS from this unvisited land cell
                    dfs(r, c)
                    count += 1  # Found a new island

        return count
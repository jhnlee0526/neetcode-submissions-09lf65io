class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        [multi‐source DFS]
        Fill each empty room (INF) in the grid with its distance to the nearest treasure (0).
        Walls are marked as -1 and remain unchanged.
        We run a multi‐source DFS from every treasure cell, pruning whenever we
        revisit a cell with an equal or shorter known distance.
            Time complexity: O(R * C)
            Space complexity: O(R * C) recursion stack in the worst case
        """
        
        if not grid or not grid[0]: # edge case
            return

        RC, CC = len(grid), len(grid[0])
        INF = 2147483647
        
        def dfs(r, c, dist):
            # base case - Stop if out of bounds or if this cell already has a shorter distance
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] < dist
            ):
                return

            # Write the new shortest distance
            grid[r][c] = dist

            # Recursion on neighbors
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                dfs(nextR, nextC, dist + 1)

        # Launch DFS() from every treasure cell
        for r in range(RC):
            for c in range(CC):
                if grid[r][c] == 0:
                    # If this cell holds a treasure (value 0),
                    # kick off a DFS from here with starting distance = 0.
                    # This DFS will flood–fill all reachable empty rooms,
                    # updating each one with its shortest distance to this treasure.
                    dfs(r, c, 0)
        
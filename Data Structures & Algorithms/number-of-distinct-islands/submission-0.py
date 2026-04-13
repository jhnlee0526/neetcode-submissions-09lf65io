class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Algorithm Type:
        #   Graph Traversal (Depth-First Search, DFS)
        #   We treat the grid as a graph where:
        #       each land cell (1) is a node
        #       edges exist between adjacent cells (up, down, left, right)
        #   DFS is used to find all cells belonging to the same island (connected component)
        #   We store island shapes using relative coordinates to detect distinct shapes

        # Time Complexity: O(R * C)
        #   Each cell is visited once during DFS.
        #   Sorting coordinates for each island collectively costs at most O(R * C log(R * C)) in worst case.

        # Space Complexity: O(R * C)
        #   visit set stores up to R*C cells
        #   recursion stack may go up to R*C in worst case (large island)
        #   uniqueIslands stores island shapes

        # Edge case: empty grid
        if not grid or not grid[0]:
            return 0

        visit = set()   # track visited cells (r, c)
        # store unique island shapes
        # each shape will be stored as tuple of relative coordinates
        uniqueIslands = set()

        RC, CC = len(grid), len(grid[0])

        # 4-directional movement
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # DFS explores entire island starting from (r,c)
        def dfs(r, c):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visit or
                grid[r][c] == 0
            ):
                return

            visit.add((r,c))
            # store relative position from island origin
            # this normalizes island shape regardless of location
            currentIsland.add((r - rOrigin, c - cOrigin))

            # explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)


        # iterate through entire grid
        for r in range(RC):
            for c in range(CC):
                # start DFS when we find unvisited land
                if (
                    grid[r][c] == 1 and 
                    (r,c) not in visit
                ):
                    currentIsland = set()   #{frozenset(), ...}

                    # starting position of island
                    rOrigin, cOrigin = r, c

                    dfs(r, c)

                    # frozenset makes it hashable (can store inside set)
                    uniqueIslands.add(frozenset(currentIsland))

        return len(uniqueIslands)
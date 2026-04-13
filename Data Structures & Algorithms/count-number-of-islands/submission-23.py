class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS recursively + hashset for visits
        #   Time : O(R × C)
        #       → Each cell is visited once at most
        #   Space: O(R × C)
        #       → HashSet for visited cells + recursion stack in worst case

        cnts = 0
        visits = set()  # Tracks visited land cells

        RC, CC = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):
            # Base case: out of bounds, water, or already visited
            if (
                r not in range(RC) or
                c not in range(CC) or
                grid[r][c] == '0' or
                (r, c) in visits
            ):
                return
            
            visits.add((r, c))  # Mark cell as visited

            # Explore all 4 directions
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                dfs(nextR, nextC)

        # Traverse the grid
        for r in range(RC):
            for c in range(CC):
                if (
                    grid[r][c] == '1' and 
                    (r, c) not in visits
                ):
                    dfs(r, c)  # Start DFS from unvisited land
                    cnts += 1  # Count one island

        return cnts
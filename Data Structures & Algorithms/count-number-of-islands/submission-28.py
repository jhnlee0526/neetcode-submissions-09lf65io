class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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

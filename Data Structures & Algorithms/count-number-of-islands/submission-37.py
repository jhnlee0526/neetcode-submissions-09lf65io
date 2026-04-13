class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs recursively + hashmap for visits
        #   time : O(r * c), visits each cells once at most 
        #   space: O(r * c), resursive stack & hashset

        # edge case
        if not grid or not grid[0]:
            return 0
        
        count = 0
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
                    count += 1

        return count


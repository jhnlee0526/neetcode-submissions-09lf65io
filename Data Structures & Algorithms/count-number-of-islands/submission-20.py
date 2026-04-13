class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs recursively + hashset for visits
        #   time : O(r * c)
        #   space: O(r * c)

        cnts = 0

        visits = set() # {(r, c), }
        RC, CC = len(grid), len(grid[0])

        def dfs(r, c): # recursively
            # base base
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                grid[r][c] == '0'
            ):
                return

            visits.add((r, c))  # visits

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    (nextR, nextC) not in visits and
                    grid[nextR][nextC] == '1'
                ):
                    dfs(nextR, nextC)


        # initial invokation of dfs()
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) not in visits and
                    grid[r][c] == '1'
                ):
                    cnts += 1
                    dfs(r, c)
        
        return cnts
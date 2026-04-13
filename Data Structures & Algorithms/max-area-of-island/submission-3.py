class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs recursively + hashmap for visits
        #   time :
        #   space:

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
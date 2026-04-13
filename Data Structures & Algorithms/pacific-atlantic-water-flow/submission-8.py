class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS recursively + hashset for visits
        #   Time  : O(r * c), each cell visited at most twice
        #   Space : O(r * c), for visited sets and recursion stack

        res = []
        pac, atl = set(), set()  # {(r, c), ..}
        RC, CC = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visits, prevH):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                heights[r][c] < prevH
            ):
                return 

            visits.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visits, heights[r][c])

        for r in range(RC):     # traverse rows (vertically)
            dfs(r, 0, pac, heights[r][0])
            dfs(r, CC - 1, atl, heights[r][CC - 1])

        for c in range(CC):     # traverse cols (horizontally)
            dfs(0, c, pac, heights[0][c])
            dfs(RC - 1, c, atl, heights[RC - 1][c])

        for r in range(RC):     # collect cells reachable by both oceans
            for c in range(CC):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
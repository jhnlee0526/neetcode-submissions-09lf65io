class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs recursively 
        #   time : O(rc)
        #   space: O(rc)

        res = []

        RC, CC = len(heights), len(heights[0])
        pac, atl = set(), set() # {(r, c), ..}

        def dfs(r, c, visits, prevH):   # recursively
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                heights[r][c] < prevH
            ):
                return
            
            visits.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    (nextR, nextC) not in visits and
                    heights[nextR][nextC] >= prevH
                ):
                    dfs(nextR, nextC, visits, heights[nextR][nextC])

        # traverse rows
        for r in range(RC):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, CC - 1, atl, heights[r][CC - 1])

        # traverse cols
        for c in range(CC):
            dfs(0, c, pac, heights[0][c])
            dfs(RC - 1, c, atl, heights[RC - 1][c])
        
        # get result
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) in pac and
                    (r, c) in atl
                ):
                    res.append([r, c])
        
        return res


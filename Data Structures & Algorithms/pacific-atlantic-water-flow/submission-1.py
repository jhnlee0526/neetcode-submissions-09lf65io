class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs recursively + two hashsets for visits: pac and atl
        #   time : O(r * c)
        #   space: O(r * c)
        
        res = []
        pac, atl = set(), set()                 # visits, {(r, c), }
        RC, CC = len(heights), len(heights[0])

        def dfs(r, c, visits, prevHeight):      # recursively
            # base case
            if (
                (r, c) in visits or
                r not in range(RC) or
                c not in range(CC) or
                heights[r][c] < prevHeight
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
                    heights[nextR][nextC] >= prevHeight
                ):
                    visits.add((r, c))
                    dfs(nextR, nextC, visits, heights[r][c])
                
        # traversing rows
        for r in range(RC):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, CC - 1, atl, heights[r][CC - 1])
        
        # traversing columns
        for c in range(CC):
            dfs(0, c, pac, heights[0][c])
            dfs(RC - 1, c, atl, heights[RC - 1][c])
        
        # getting results
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) in pac and
                    (r, c) in atl
                ):
                    res.append([r, c])

        return res
            


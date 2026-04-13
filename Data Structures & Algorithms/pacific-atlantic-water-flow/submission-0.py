class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs recursively + TWO hashsets for visits on pacific and atlantic
        #   time : O(R * C)
        #   space: O(R * C)
        
        res = []

        pac, atl = set(), set()         # visits
        RC, CC = len(heights), len(heights[0])

        def dfs(r, c, visit, prevH):    # recursively
            # base case
            if (
                (r, c) in visit or
                r not in range(RC) or
                c not in range(CC) or
                heights[r][c] < prevH
            ):
                return
            
            visit.add((r, c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                dfs(nextR, nextC, visit, heights[r][c])

        # traverse each row for dfs each
        for r in range(RC):
            dfs(r, 0, pac, heights[r][0])            # starting from the (r, 0)
            dfs(r, CC - 1, atl, heights[r][CC - 1])  # starting from the (r, last-index)
        
        # traverse each col for dfs each
        for c in range(CC):
            dfs(0, c, pac, heights[0][c])            # starting from the (0, c)
            dfs(RC - 1, c, atl, heights[RC - 1][c])  # starting form the (last-index, c)
        
        # getting result
        for r in range(RC):
            for c in range(CC):
                if (
                    (r , c) in pac and 
                    (r, c) in atl
                ):
                    res.append([r, c])
        return res
        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ✅ DFS recursively
        #   Time : O(R × C)
        #       → Each cell is visited at most once per ocean
        #   Space: O(R × C)
        #       → Visited sets + recursion stack in worst case

        res = []
        
        RC, CC = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        pac, atl = set(), set()     # {(r, c), ..}
        
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
                nextR, nextC = r + dr, c + dc
                dfs(nextR, nextC, visits, heights[r][c])

        # traverse rows (vertically)
        for r in range(RC):
            dfs(r, 0, pac, heights[r][0])         # Pacific
            dfs(r, CC - 1, atl, heights[r][CC - 1])  # Atlantic

        # traverse cols (horizontally)
        for c in range(CC):
            dfs(0, c, pac, heights[0][c])         # Pacific
            dfs(RC - 1, c, atl, heights[RC - 1][c])  # Atlantic

        # get the result
        for r in range(RC):
            for c in range(CC):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
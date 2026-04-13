class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS iteratively + visits(hashset) for pac, atl
        #   Time Complexity: O(R × C)
        #       - Each cell is visited at most once per ocean
        #   Space Complexity: O(R × C)
        #       - Sets to track visited cells + recursion stack

        # edge case
        if not heights or not heights:
            return []
        
        res = []
        
        pac, atl = set(), set()

        RC, CC = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c, visits, prevH):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                heights[r][c] < prevH or
                (r, c) in visits
            ):
                return

            visits.add((r, c))

            for dr, dc in directions:
                nextR, nextC = r + dr, c + dc
                if (
                    nextR in range(RC) and
                    nextC in range(CC) and
                    (nextR, nextC) not in visits and
                    heights[nextR][nextC] >= prevH
                ):
                    dfs(nextR, nextC, visits, heights[nextR][nextC])

        
        # traverse rows & cols for dfs()
        for r in range(RC):
            dfs(r, 0, pac, heights[r][0])   # r, c, visits, prevH
            dfs(r, CC - 1, atl, heights[r][CC - 1])
        for c in range(CC):
            dfs(0, c, pac, heights[0][c])
            dfs(RC - 1, c, atl, heights[RC -1][c])

        # get result
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) in pac and
                    (r, c) in atl
                ):
                    res.append([r, c])
        return res

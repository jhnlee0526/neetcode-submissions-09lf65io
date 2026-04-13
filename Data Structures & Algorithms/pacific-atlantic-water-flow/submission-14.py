class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # graph: BFS iteratively with queue + hashset for visits
        #   time : O(R * C), visits each cells at once
        #   space: O(R * C), hashset for visits

        if not heights or not heights[0]:
            return []
        
        res = []
        RC, CC = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        pac, atl = set(), set() # {(r, c), ..}
        
        def bfs(r, c, visits):
            q = deque([(r, c, heights[r][c])]) # [(r, c, prevHeight), ..]
            visits.add((r, c))

            while q:
                qr, qc, qh = q.popleft()
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if (
                        nr in range(RC) and
                        nc in range(CC) and
                        (nr, nc) not in visits and
                        heights[nr][nc] >= qh
                    ):
                        q.append((nr, nc, heights[nr][nc]))
                        visits.add((nr, nc))

            
        for r in range(RC):
            bfs(r, 0, pac)
            bfs(r, CC - 1, atl)
        
        for c in range(CC):
            bfs(0, c, pac)
            bfs(RC - 1, c, atl)


        for r in range(RC):
            for c in range(CC):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


        #---------------------------
        # graph: DFS recursively + hashset for visits
        #   time : O(R * C), visits each cells at once
        #   space: O(R * C), hashset for visits & recursive stacks

        if not heights or not heights[0]:   # edge case
            return []
        
        res = []

        RC, CC = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        pac = set() # {(r, c), ..}
        atl = set() 

        def dfs(r, c, visits, prevHeight):
            # base case
            if (
                r not in range(RC) or
                c not in range(CC) or
                (r, c) in visits or
                heights[r][c] < prevHeight
            ):
                return
            
            visits.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visits, heights[r][c])


        for r in range(RC):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, CC - 1, atl, heights[r][CC - 1])

        for c in range(CC):
            dfs(0, c, pac, heights[0][c])
            dfs(RC - 1, c, atl, heights[RC - 1][c])    


        for r in range(RC):
            for c in range(CC):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
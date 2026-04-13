class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs iteratively with queue + hashmap for visits
        #   time : O(r * c)
        #   space: O(r * c)

        if not heights or not heights[0]:
            return []

        res = []

        pac = set() # {(r, c), ..}
        atl = set() # {(r, c), ..}

        RC, CC = len(heights), len(heights[0])
        directions = [[1, 0],[-1, 0], [0, 1], [0, -1]]

        def bfs(r, c, visits):
            q = deque([(r, c, heights[r][c])])   # [(r, c, prev height), ..]
            visits.add((r, c))

            while q:
                qr, qc, qh = q.popleft()
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    if (
                        nr in range(RC) and
                        nc in range(CC) and
                        (nr, nc) not in visits and
                        qh <= heights[nr][nc]
                    ):
                        q.append((nr, nc, heights[nr][nc]))
                        visits.add((nr, nc))
        
        ###
        for r in range(RC):
            bfs(r, 0, pac)      # left
            bfs(r, CC - 1, atl) # right
        for c in range(CC):
            bfs(0, c, pac)      # top
            bfs(RC - 1, c, atl) # bottom

        # get res for result
        for r in range(RC):
            for c in range(CC):
                if (
                    (r, c) in pac and
                    (r, c) in atl
                ):
                    res.append([r, c])

        return res
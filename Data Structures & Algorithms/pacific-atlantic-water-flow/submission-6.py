class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ✅ BFS iteratively with queue
        #   Time : O(R × C)
        #       → Each cell is visited at most once per ocean
        #   Space: O(R × C)
        #       → Visited sets + queue in worst case

        res = []
        
        RC, CC = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        pac, atl = set(), set()     # {(r, c), ..}
        
        def bfs(r, c, visits):
            q = deque()             # [(r, c), ..]
            
            q.append((r, c))
            visits.add((r, c))
            
            while q:
                qr, qc = q.popleft()
                for dr, dc in directions:
                    nextR, nextC = qr + dr, qc + dc
                    if (
                        nextR in range(RC) and
                        nextC in range(CC) and
                        (nextR, nextC) not in visits and
                        heights[nextR][nextC] >= heights[qr][qc]   ##
                    ):
                        q.append((nextR, nextC))
                        visits.add((nextR, nextC))

        # traverse rows (vertically)
        for r in range(RC):
            bfs(r, 0, pac)
            bfs(r, CC - 1, atl)

        # traverse cols (horizontally)
        for c in range(CC):
            bfs(0, c, pac)
            bfs(RC - 1, c, atl)

        # get the result
        for r in range(RC):
            for c in range(CC):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res